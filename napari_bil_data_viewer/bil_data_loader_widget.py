# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:49:37 2021

@author: alpha

Roadmap:
- Improve the performance
- Migrate to npe2
- Do loading in separate thread
- Write the tests
"""

import random
import string
import napari
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
import dask.array as da
import fsspec
import requests
from bs4 import BeautifulSoup
from skimage import io
from dask import delayed
import tifffile
from .dataset_info import get_datasets
from .fMOST_datasets import datasets
from .dataset_metadata import dataset_metadata
from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QMovie
from qtpy.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit, QCheckBox, QSpacerItem, QScrollArea, QGroupBox, QFormLayout
)
from napari.plugins.io import read_data_with_plugins
from napari.qt.threading import thread_worker
from napari.utils.colormaps import label_colormap

color_map = label_colormap(num_colors=500, seed=0.5)


class LoadCuratedDatasets(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.image_layer = None
        self.soma_layer = None
        self.tracings_layer = None
        self.datasets = sorted([key for key in get_datasets()])
        self.dataset = "mouseID_19032508-191171" if len(self.datasets) else None
        self.swc_url = ""
        self.visualized_tracings = []
        self.neuron_sections = []
        self.load_button = QPushButton("Load Dataset")
        self.spinner_label = SpinnerLabel()
        self.swc_checkboxes = []
        self.init_ui()
        napari_viewer.layers.events.removed.connect(self._on_layer_deletion)
        napari_viewer.layers.events.removing.connect(self._pre_layer_deletion)

    def init_ui(self):
        # create widgets
        dataset_label = QLabel("Select Dataset:")
        self.dataset_at_bil_label = QLabel(f'<a href="{self.url_at_bil}" style="color:gray;">on BIL website</a>')
        self.dataset_at_bil_label.setOpenExternalLinks(True)
        self.dataset_at_bil_label.setToolTip("view selected dataset on BIL website")
        self.metadata_label = QLabel(f'<a href="{self.metadata_url}" style="color:gray;">metadata</a>')
        self.metadata_label.setOpenExternalLinks(True)
        self.metadata_label.setToolTip("view metadata for selected dataset on BIL website")
        dataset_dropdown = QComboBox()
        dataset_dropdown.addItems(self.datasets)
        dataset_dropdown.setToolTip("summary fMOST datasets")
        dataset_dropdown.currentTextChanged.connect(self.on_combobox_changed)

        # ----------------------- SWC controls -----------------------
        vbox_swc = QVBoxLayout()

        hbox_swc = QHBoxLayout()
        hbox_swc.addLayout(vbox_swc)

        scroll = QScrollArea()
        swc_groupbox = QGroupBox('pre-loaded neurons')
        swc_form = QFormLayout()
        swc_groupbox.setLayout(swc_form)
        scroll.setWidget(swc_groupbox)
        scroll.setWidgetResizable(True)
        scroll.setMinimumHeight(200)
        vscroll = QVBoxLayout()
        vscroll.addWidget(scroll)
        hscroll = QHBoxLayout()
        hscroll.addLayout(vscroll)
        vbox_scrollarea = QVBoxLayout()
        vbox_scrollarea.addLayout(hscroll)
        hbox_scrollarea = QHBoxLayout()
        hbox_scrollarea.addLayout(vbox_scrollarea)

        # ----------------------- Create layout -----------------------
        vbox_main = QVBoxLayout()
        hbox_dataset = QHBoxLayout()

        hbox_dataset_label = QHBoxLayout()
        hbox_dataset_label.addWidget(dataset_label)
        hbox_dataset_dropdown = QHBoxLayout()
        hbox_dataset_dropdown.addWidget(dataset_dropdown)
        hbox_dataset_at_bil_label = QHBoxLayout()
        hbox_dataset_at_bil_label.addWidget(self.dataset_at_bil_label)
        hbox_dataset_at_bil_label.addWidget(self.metadata_label)
        hbox_dataset_load_btn = QHBoxLayout()
        hbox_dataset_load_btn.addWidget(self.load_button)

        vbox_dataset = QVBoxLayout()
        vbox_dataset.addLayout(hbox_dataset_label)
        vbox_dataset.addLayout(hbox_dataset_dropdown)
        vbox_dataset.addLayout(hbox_dataset_at_bil_label)
        vbox_dataset.addItem(QSpacerItem(1, 10))
        vbox_dataset.addLayout(hbox_dataset_load_btn)
        vbox_dataset.addItem(QSpacerItem(1, 25))

        hbox_dataset.addLayout(vbox_dataset)

        hbox_spinner = QHBoxLayout()
        hbox_spinner.addWidget(self.spinner_label)

        vbox_main.addLayout(BILInfoHbox())
        vbox_main.addItem(QSpacerItem(1, 25))
        vbox_main.addLayout(hbox_spinner)
        vbox_main.addLayout(hbox_dataset)
        vbox_main.addLayout(hbox_scrollarea)
        vbox_main.addItem(QSpacerItem(1, 10))
        vbox_main.addLayout(hbox_swc)

        # dynamically add checkboxes for SWC files
        dataset_dropdown.currentIndexChanged.connect(lambda: self.create_swc_checkboxes(dataset_dropdown.currentText(), swc_form))
        dataset_dropdown.setCurrentIndex(self.datasets.index(self.dataset))

        self.setLayout(vbox_main)

        # connect signals and slots
        self.load_button.clicked.connect(self.load_dataset)

    def load_dataset(self):

        def _show_img(args):
            data, meta, layer_type = args
            if self.image_layer and self.image_layer in self.viewer.layers:
                self.viewer.layers.remove(self.image_layer)
            if self.tracings_layer and self.tracings_layer in self.viewer.layers:
                self.viewer.layers.remove(self.tracings_layer)
            if self.soma_layer and self.soma_layer in self.viewer.layers:
                self.viewer.layers.remove(self.soma_layer)
            self.image_layer = self.viewer.add_image(data, **meta)
            self.spinner_label.movie().stop()
            self.spinner_label.setHidden(True)
            self.load_button.setEnabled(True)

        @thread_worker(connect={"returned": _show_img})
        def _load_img():
            dataset_info = get_datasets()[self.dataset]
            dataset_name = self.dataset
            return load_bil_data(dataset_info, dataset_name)

        self.load_button.setEnabled(False)
        self.spinner_label.setHidden(False)
        self.spinner_label.movie().start()
        _load_img()

    def on_combobox_changed(self, value):
        self.dataset = value
        self.dataset_at_bil_label.setText(f'<a href="{self.url_at_bil}" style="color:gray;">on BIL website</a>')
        self.metadata_label.setText(f'<a href="{self.metadata_url}" style="color:gray;">metadata</a>')

    def load_swc(self, url=None):
        import numpy as np
        from napari.layers.shapes import Shapes

        if not url:
            url = self.swc_url

        points, shapes = load_bil_swc(url, datasets.get(self.dataset, get_datasets()[self.dataset]))
        data, meta, __ = shapes
        self.neuron_sections.append(len(data))
        soma, soma_meta, __ = points
        labels_color = next(color_generator)
        meta["edge_color"] = labels_color[:3].reshape(1, 3)
        if not self.tracings_layer or 'neuron tracings' not in self.viewer.layers:
            self.tracings_layer = Shapes(ndim=3, **meta)
            self.viewer.layers.append(self.tracings_layer)
        self.tracings_layer.add_paths(data, edge_color=labels_color)
        if self.soma_layer and 'soma' in self.viewer.layers:
            self.soma_layer.add(soma)
        else:
            self.soma_layer = self.viewer.add_points(soma, **soma_meta)
        self.visualized_tracings.append(url)

    def create_swc_checkboxes(self, dataset_name, vbox):
        # remove existing checkboxes
        for checkbox in self.swc_checkboxes:
            vbox.removeWidget(checkbox)
            checkbox.setParent(None)

        # get SWC files for selected dataset
        swc_files = get_swc_files(dataset_name)

        # create checkboxes for each SWC file
        for swc_file in swc_files:
            checkbox = QCheckBox(shorten_swc_path(swc_file))
            checkbox.setToolTip("best if vewed in 3D")
            vbox.addWidget(checkbox)
            self.swc_checkboxes.append(checkbox)
            checkbox.stateChanged.connect(lambda state, path=swc_file: self.visualize_swc(path, state))

    def visualize_swc(self, path_to_swc, state):
        print("state", state)
        if state == Qt.Checked:
            print(f"Visualizing {path_to_swc}")
            self.load_swc(path_to_swc)
        else:
            print(f"Hiding {path_to_swc}")
            self.hide_swc(path_to_swc)

    def add_checkbox(self, vbox, swc_file_path):
        if swc_file_path:
            checkbox = QCheckBox(shorten_swc_path(swc_file_path))
            checkbox.setToolTip("best if vewed in 3D")
            checkbox.setChecked(True)
            vbox.addWidget(checkbox)
            checkbox.stateChanged.connect(lambda state, path=swc_file_path: self.visualize_swc(path, state))
            self.swc_checkboxes.append(checkbox)
            self.load_swc(swc_file_path)

    def add_checkboxes(self, vbox, url):
        # Check if the URL leads to a folder or a file
        if url.endswith('.swc'):
            self.add_checkbox(vbox, url)
        else:
            # assume folder with swc
            swc_files = getFilesHttp(url, 'swc')
            self.add_folder_checkboxes(vbox, swc_files)

    def add_folder_checkboxes(self, vbox, swc_files):
        # add a checkbox for each SWC file when URL points to a folder with multiple swc
        for swc_file in swc_files:
            self.add_checkbox(vbox, swc_file)

    def hide_swc(self, url):
        """
        Hide unchecked neuron tracing.

        Remove soma point from points layer, and paths from shapes layer.
        :param url:
        :return:
        """
        layer_data = self.tracings_layer.data
        url_index = self.visualized_tracings.index(url)
        self.soma_layer.selected_data = set([url_index])
        self.soma_layer.remove_selected()
        start_index = sum(self.neuron_sections[:url_index])
        end_index = start_index + self.neuron_sections[url_index]
        print(start_index, end_index)
        del layer_data[start_index:end_index]
        self.tracings_layer.data = layer_data
        self.visualized_tracings.pop(url_index)
        self.neuron_sections.pop(url_index)

    def _on_layer_deletion(self, e):
        layer_name = e.value.name
        if layer_name == 'soma' or layer_name == 'neuron tracings':
            self.uncheck_swc_checkboxes()

    def _pre_layer_deletion(self, e):
        pass

    def uncheck_swc_checkboxes(self):
        for checkbox in self.swc_checkboxes:
            checkbox.setChecked(False)

    @property
    def url_at_bil(self):
        try:
            url = datasets[self.dataset]['url'][0]
            url = url[:url.rfind('/')]
        except (KeyError, IndexError):
            url = ""
        return url

    @property
    def metadata_url(self):
        return dataset_metadata.get(self.dataset, "#")


class LayerScaleControls(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.layer_to_adjust_scale = ""
        self.adjusted_scale_z = 1
        self.adjusted_scale_y = 1
        self.adjusted_scale_x = 1
        self.init_ui()
        napari_viewer.layers.selection.events.changed.connect(self._on_selection)
        napari_viewer.layers.events.removed.connect(self._on_layer_deletion)

    def init_ui(self):
        # ----------------------- Scale Controls -----------------------
        hbox_scale_label = QHBoxLayout()
        scale_label = QLabel("Adjust Scale:")
        hbox_scale_label.addWidget(scale_label)

        hbox_scale = QHBoxLayout()
        z_scale_input_label = QLabel("z :")
        z_scale_input_label.setFixedWidth(20)
        self.z_scale_input = QLineEdit()
        self.z_scale_input.setPlaceholderText("1.0")
        self.z_scale_input.setFixedWidth(100)
        self.z_scale_input.textChanged.connect(self.on_scale_z_input_changed)
        y_scale_input_label = QLabel("y :")
        y_scale_input_label.setFixedWidth(20)
        self.y_scale_input = QLineEdit()
        self.y_scale_input.setPlaceholderText("1.0")
        self.y_scale_input.setFixedWidth(100)
        self.y_scale_input.textChanged.connect(self.on_scale_y_input_changed)
        x_scale_input_label = QLabel("x :")
        x_scale_input_label.setFixedWidth(20)
        self.x_scale_input = QLineEdit()
        self.x_scale_input.setPlaceholderText("1.0")
        self.x_scale_input.setFixedWidth(100)
        self.x_scale_input.textChanged.connect(self.on_scale_x_input_changed)
        hbox_scale.addWidget(z_scale_input_label)
        hbox_scale.addWidget(self.z_scale_input)
        hbox_scale.addWidget(y_scale_input_label)
        hbox_scale.addWidget(self.y_scale_input)
        hbox_scale.addWidget(x_scale_input_label)
        hbox_scale.addWidget(self.x_scale_input)

        hbox_scale_dropdown = QHBoxLayout()
        scale_dropdown_label = QLabel("layer:")
        scale_dropdown_label.setFixedWidth(50)
        self.scale_dropdown = QComboBox()
        self.scale_dropdown.currentTextChanged.connect(self.on_scale_dropdown_changed)
        self.scale_dropdown.addItems([x.name for x in self.viewer.layers])
        self.scale_dropdown.setToolTip("select layer to be rescaled")
        hbox_scale_dropdown.addWidget(scale_dropdown_label)
        hbox_scale_dropdown.addWidget(self.scale_dropdown)

        hbox_adjust_scale_btn = QHBoxLayout()
        adjust_scale_btn = QPushButton("Adjust")
        adjust_scale_btn.clicked.connect(self.adjust_scale)
        hbox_adjust_scale_btn.addWidget(adjust_scale_btn)

        vbox_scale = QVBoxLayout()
        vbox_scale.addLayout(hbox_scale_label)
        vbox_scale.addLayout(hbox_scale_dropdown)
        vbox_scale.addLayout(hbox_scale)
        vbox_scale.addLayout(hbox_adjust_scale_btn)

        hbox_scale_controls = QHBoxLayout()
        hbox_scale_controls.addLayout(vbox_scale)

        vbox_main = QVBoxLayout()
        vbox_main.addLayout(hbox_scale_controls)

        self.setLayout(vbox_main)

    def on_scale_dropdown_changed(self, value):
        if value != "":
            self.layer_to_adjust_scale = value
            scale_z, scale_y, scale_x = self.viewer.layers[value].scale[-3:]
            self.adjusted_scale_z = scale_z
            self.adjusted_scale_y = scale_y
            self.adjusted_scale_x = scale_x
            self.z_scale_input.setText(str(scale_z))
            self.y_scale_input.setText(str(scale_y))
            self.x_scale_input.setText(str(scale_x))

    def on_scale_z_input_changed(self, value):
        self.adjusted_scale_z = value

    def on_scale_y_input_changed(self, value):
        self.adjusted_scale_y = value

    def on_scale_x_input_changed(self, value):
        self.adjusted_scale_x = value

    def _on_selection(self):
        self.scale_dropdown.clear()
        self.scale_dropdown.addItems([x.name for x in self.viewer.layers])

    def _on_layer_deletion(self):
        self.scale_dropdown.clear()
        self.z_scale_input.clear()
        self.y_scale_input.clear()
        self.x_scale_input.clear()

    def adjust_scale(self):
        print("Changing scale of", self.layer_to_adjust_scale, "to", self.adjusted_scale_z, self.adjusted_scale_y, self.adjusted_scale_x)
        self.viewer.layers[self.layer_to_adjust_scale].scale = [
            self.adjusted_scale_z,
            self.adjusted_scale_y,
            self.adjusted_scale_x
        ]


class LoadMultiscaleDataFromURL(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.fullresolution_url = ""
        self.example_url = "https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr"
        self.spinner_label = SpinnerLabel()
        self.init_ui()

    def init_ui(self):
        fullresolution_label = QLabel("Visualize multi-scale data (.zarr):")
        self.url_input_fullresolution = QLineEdit()
        self.url_input_fullresolution.setPlaceholderText("paste URL")
        self.url_input_fullresolution.setToolTip(f"example: {self.example_url}")
        self.url_input_fullresolution.textChanged.connect(self.on_fullresolution_url_changed)
        paste_example_url_label = QLabel('<a href="#" style="color:gray;">paste example URL</a>')
        paste_example_url_label.linkActivated.connect(self._on_paste_example_url_clicked)
        clear_label = QLabel('<a href="#" style="color:gray;">clear</a>')
        clear_label.linkActivated.connect(self._on_clear_clicked)
        self.button_fullresolution = QPushButton("Load Dataset")
        self.button_fullresolution.clicked.connect(self.load_full_resolution)

        hbox_fullresolution_label = QHBoxLayout()
        hbox_fullresolution_label.addWidget(fullresolution_label)
        hbox_fullresolution_url_input = QHBoxLayout()
        hbox_fullresolution_url_input.addWidget(self.url_input_fullresolution)
        hbox_paste_example_url_label = QHBoxLayout()
        hbox_paste_example_url_label.addWidget(clear_label)
        hbox_paste_example_url_label.addWidget(paste_example_url_label)
        hbox_fullresolution_show_button = QHBoxLayout()
        hbox_fullresolution_show_button.addWidget(self.button_fullresolution)

        vbox_fullresolution = QVBoxLayout()
        vbox_fullresolution.addLayout(hbox_fullresolution_label)
        vbox_fullresolution.addLayout(hbox_fullresolution_url_input)
        vbox_fullresolution.addLayout(hbox_paste_example_url_label)
        vbox_fullresolution.addLayout(hbox_fullresolution_show_button)

        hbox_fullresolution = QHBoxLayout()
        hbox_fullresolution.addLayout(vbox_fullresolution)

        # Loading indicator (spinner)
        hbox_spinner = QHBoxLayout()
        hbox_spinner.addWidget(self.spinner_label)

        vbox_main = QVBoxLayout()
        vbox_main.addLayout(BILInfoHbox())
        vbox_main.addItem(QSpacerItem(1, 25))
        vbox_main.addLayout(hbox_spinner)
        vbox_main.addLayout(hbox_fullresolution)

        self.setLayout(vbox_main)

    def on_fullresolution_url_changed(self, value):
        self.fullresolution_url = value

    def load_full_resolution(self):
        def _show_img(layers):
            for layer in layers:
                data, meta, layer_type = layer
                self.viewer.add_image(data, **meta)  # list of layers
            self.spinner_label.movie().stop()
            self.spinner_label.setHidden(True)
            self.button_fullresolution.setEnabled(True)

        @thread_worker(connect={"returned": _show_img})
        def _load_img():
            layer_data, hookimpl = read_data_with_plugins(
                [self.fullresolution_url], plugin="napari-ome-zarr", stack=False
            )
            return layer_data

        self.button_fullresolution.setEnabled(False)
        self.spinner_label.setHidden(False)
        self.spinner_label.movie().start()
        _load_img()

    def _on_paste_example_url_clicked(self):
        self.url_input_fullresolution.setText(self.example_url)

    def _on_clear_clicked(self):
        self.url_input_fullresolution.setText("")


class LoadImageStackFromURL(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.example_url = "https://download.brainimagelibrary.org/56/fb/56fb1b25ca6b5fae/OTR-Venus/OTR-Venus_P14_F5/stitchedImage_ch2/"
        self.spinner_label = SpinnerLabel()
        self.init_ui()

    def init_ui(self):
        self.dataset_url_input = QLineEdit()
        self.dataset_url_input.setPlaceholderText("paste URL")
        self.dataset_url_input.setToolTip(f"example: {self.example_url}")
        self.dataset_url_input.textChanged.connect(self.on_dataset_url_changed)
        paste_example_url_label = QLabel('<a href="#" style="color:gray;">paste example URL</a>')
        paste_example_url_label.linkActivated.connect(self._on_paste_example_url_clicked)
        clear_label = QLabel('<a href="#" style="color:gray;">clear</a>')
        clear_label.linkActivated.connect(self._on_clear_clicked)
        dataset_url_label = QLabel("Load image stack (tif, tiff, jp2):")
        self.load_button = QPushButton("Load Dataset")
        self.load_button.clicked.connect(self.load_dataset)

        # Loading indicator (spinner)
        hbox_spinner = QHBoxLayout()
        hbox_spinner.addWidget(self.spinner_label)

        hbox_paste_example_url_label = QHBoxLayout()
        hbox_paste_example_url_label.addWidget(clear_label)
        hbox_paste_example_url_label.addWidget(paste_example_url_label)

        vbox_main = QVBoxLayout()
        vbox_main.addLayout(BILInfoHbox())
        vbox_main.addItem(QSpacerItem(1, 25))
        vbox_main.addWidget(dataset_url_label)
        vbox_main.addLayout(hbox_spinner)
        vbox_main.addWidget(self.dataset_url_input)
        vbox_main.addLayout(hbox_paste_example_url_label)
        vbox_main.addWidget(self.load_button)

        self.setLayout(vbox_main)

    def on_dataset_url_changed(self, value):
        self.dataset_url = value

    def load_dataset(self):

        def _show_img(args):
            data, meta, layer_type = args
            self.viewer.add_image(data, **meta)
            self.spinner_label.movie().stop()
            self.spinner_label.setHidden(True)
            self.load_button.setEnabled(True)

        @thread_worker(connect={"returned": _show_img})
        def _load_img():
            dataset_info = {
                'contrast_limits': [0, 65535],
                'scale': (1, 1, 1),
                'url': [
                    self.dataset_url
                ]
            }
            dataset_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
            return load_bil_data(dataset_info, dataset_name)

        self.load_button.setEnabled(False)
        self.spinner_label.setHidden(False)
        self.spinner_label.movie().start()
        _load_img()

    def _on_paste_example_url_clicked(self):
        self.dataset_url_input.setText(self.example_url)

    def _on_clear_clicked(self):
        self.dataset_url_input.setText("")


class LoadNeuronMorphologyFromURL(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.soma_layer = None
        self.tracings_layer = None
        self.swc_checkboxes = []
        self.visualized_tracings = []
        self.neuron_sections = []
        self.example_url = "https://download.brainimagelibrary.org/3a/c1/3ac1bdc022d0da78/191171-20/mouseID_191171_20.swc"
        self.init_ui()

    def init_ui(self):
        swc_url_label = QLabel("Load neuron morphology (.swc) from URL:")
        hbox_swc_url_label = QHBoxLayout()
        hbox_swc_url_label.addWidget(swc_url_label)

        self.swc_url_input = QLineEdit()
        self.swc_url_input.setPlaceholderText("paste URL")
        self.swc_url_input.setToolTip(f"example: {self.example_url}")
        self.swc_url_input.textChanged.connect(self.on_swc_url_changed)
        paste_example_url_label = QLabel('<a href="#" style="color:gray;">paste example URL</a>')
        paste_example_url_label.linkActivated.connect(self._on_paste_example_url_clicked)
        clear_label = QLabel('<a href="#" style="color:gray;">clear</a>')
        clear_label.linkActivated.connect(self._on_clear_clicked)
        show_swc_button = QPushButton("Show SWC")
        show_swc_button.clicked.connect(lambda: self.add_checkboxes(vbox_swc, self.swc_url_input.text()))

        hbox_show_swc_btn = QHBoxLayout()
        hbox_show_swc_btn.addWidget(show_swc_button)

        hbox_swc_url_input = QHBoxLayout()
        hbox_swc_url_input.addWidget(self.swc_url_input)

        hbox_paste_example_url_label = QHBoxLayout()
        hbox_paste_example_url_label.addWidget(clear_label)
        hbox_paste_example_url_label.addWidget(paste_example_url_label)

        vbox_swc = QVBoxLayout()
        vbox_swc.addLayout(hbox_swc_url_label)
        vbox_swc.addLayout(hbox_swc_url_input)
        vbox_swc.addLayout(hbox_paste_example_url_label)
        vbox_swc.addLayout(hbox_show_swc_btn)

        hbox_swc = QHBoxLayout()
        hbox_swc.addLayout(vbox_swc)

        vbox_main = QVBoxLayout()
        vbox_main.addLayout(BILInfoHbox())
        vbox_main.addItem(QSpacerItem(1, 25))
        vbox_main.addLayout(hbox_swc)

        self.setLayout(vbox_main)

    def add_checkbox(self, vbox, swc_file_path):
        if swc_file_path:
            checkbox = QCheckBox(shorten_swc_path(swc_file_path))
            checkbox.setChecked(True)
            checkbox.setToolTip("best if viewed in 3D")
            vbox.addWidget(checkbox)
            checkbox.stateChanged.connect(lambda state, path=swc_file_path: self.visualize_swc(path, state))
            self.swc_checkboxes.append(checkbox)
            self.load_swc(swc_file_path)

    def visualize_swc(self, path_to_swc, state):
        print("state", state)
        if state == Qt.Checked:
            print(f"Visualizing {path_to_swc}")
            self.load_swc(path_to_swc)
        else:
            print(f"Hiding {path_to_swc}")
            self.hide_swc(path_to_swc)

    def add_checkboxes(self, vbox, url):
        # Check if the URL leads to a folder or a file
        if url.endswith('.swc'):
            self.add_checkbox(vbox, url)
        else:
            # assume folder with swc
            swc_files = getFilesHttp(url, 'swc')
            self.add_folder_checkboxes(vbox, swc_files)

    def add_folder_checkboxes(self, vbox, swc_files):
        # add a checkbox for each SWC file when URL points to a folder with multiple swc
        for swc_file in swc_files:
            self.add_checkbox(vbox, swc_file)

    def on_swc_url_changed(self, value):
        self.swc_url = value

    def load_swc(self, url=None):
        import numpy as np
        from napari.layers.shapes import Shapes

        if not url:
            url = self.swc_url

        points, shapes = load_bil_swc(url, {"scale": [1, 1, 1]})
        data, meta, __ = shapes
        meta['name'] = 'neuron tracings (URL)'
        self.neuron_sections.append(len(data))
        soma, soma_meta, __ = points
        soma_meta['name'] = 'soma (URL)'
        labels_color = next(color_generator)
        meta["edge_color"] = labels_color[:3].reshape(1, 3)
        if not self.tracings_layer or 'neuron tracings (URL)' not in self.viewer.layers:
            self.tracings_layer = Shapes(ndim=3, **meta)
            self.viewer.layers.append(self.tracings_layer)
        self.tracings_layer.add_paths(data, edge_color=labels_color)
        if self.soma_layer and 'soma (URL)' in self.viewer.layers:
            self.soma_layer.add(soma)
        else:
            self.soma_layer = self.viewer.add_points(soma, **soma_meta)
        self.visualized_tracings.append(url)

    def hide_swc(self, url):
        """
        Hide unchecked neuron tracing.

        Remove soma point from points layer, and paths from shapes layer.
        :param url:
        :return:
        """
        layer_data = self.tracings_layer.data
        url_index = self.visualized_tracings.index(url)
        self.soma_layer.selected_data = set([url_index])
        self.soma_layer.remove_selected()
        start_index = sum(self.neuron_sections[:url_index])
        end_index = start_index + self.neuron_sections[url_index]
        print(start_index, end_index)
        del layer_data[start_index:end_index]
        self.tracings_layer.data = layer_data
        self.visualized_tracings.pop(url_index)
        self.neuron_sections.pop(url_index)

    def _on_paste_example_url_clicked(self):
        self.swc_url_input.setText(self.example_url)

    def _on_clear_clicked(self):
        self.swc_url_input.setText("")


class LoadHistologyImageFromURL(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.example_url = "https://download.brainimagelibrary.org/ae/ad/aead64733884e4c6/pRF1sMBiF024d211023tNISSLnPuck_210218_08/pRF1sMBiF024d211023tNISSLnPuck_210218_08POST.tif"
        self.spinner_label = SpinnerLabel()
        self.init_ui()

    def init_ui(self):
        self.dataset_url_input = QLineEdit()
        self.dataset_url_input.setPlaceholderText("paste URL")
        self.dataset_url_input.setToolTip(f"example: {self.example_url}")
        self.dataset_url_input.textChanged.connect(self.on_dataset_url_changed)
        paste_example_url_label = QLabel('<a href="#" style="color:gray;">paste example URL</a>')
        paste_example_url_label.linkActivated.connect(self._on_paste_example_url_clicked)
        clear_label = QLabel('<a href="#" style="color:gray;">clear</a>')
        clear_label.linkActivated.connect(self._on_clear_clicked)
        dataset_url_label = QLabel("Load image (tif, tiff):")
        self.load_button = QPushButton("Load Dataset")
        self.load_button.clicked.connect(self.load_dataset)

        # Loading indicator (spinner)
        hbox_spinner = QHBoxLayout()
        hbox_spinner.addWidget(self.spinner_label)

        hbox_paste_example_url_label = QHBoxLayout()
        hbox_paste_example_url_label.addWidget(clear_label)
        hbox_paste_example_url_label.addWidget(paste_example_url_label)

        vbox_main = QVBoxLayout()
        vbox_main.addLayout(BILInfoHbox())
        vbox_main.addItem(QSpacerItem(1, 25))
        vbox_main.addWidget(dataset_url_label)
        vbox_main.addLayout(hbox_spinner)
        vbox_main.addWidget(self.dataset_url_input)
        vbox_main.addLayout(hbox_paste_example_url_label)
        vbox_main.addWidget(self.load_button)

        self.setLayout(vbox_main)

    def on_dataset_url_changed(self, value):
        self.dataset_url = value

    def load_dataset(self):

        def _show_img(args):
            data, meta, layer_type = args
            self.viewer.add_image(data, **meta)
            self.spinner_label.movie().stop()
            self.spinner_label.setHidden(True)
            self.load_button.setEnabled(True)

        @thread_worker(connect={"returned": _show_img})
        def _load_img():
            dataset_info = {
                'contrast_limits': [0, 255],
                'scale': (1, 1),
                'url': [
                    self.dataset_url
                ]
            }
            dataset_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
            return load_single_image(dataset_info, dataset_name)

        self.load_button.setEnabled(False)
        self.spinner_label.setHidden(False)
        self.spinner_label.movie().start()
        _load_img()

    def _on_paste_example_url_clicked(self):
        self.dataset_url_input.setText(self.example_url)

    def _on_clear_clicked(self):
        self.dataset_url_input.setText("")



def get_swc_files(dataset_name):
    from .fMOST_swc import swc_datasets
    swc_files = swc_datasets.get(dataset_name, [])
    return swc_files


def shorten_swc_path(path):
    split_path = path.split("/")
    return split_path[-1] if len(split_path) else path


def getFilesHttp(url: str, ext: str) -> list:
    def listFD(url, ext=''):
        page = requests.get(url).text
        # print(page)
        soup = BeautifulSoup(page, 'html.parser')
        return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    files = []
    for file in listFD(url, ext):
        files.append(file)

    return files


def getImage(fileObj):
    with fileObj as f:
        print('Reading {} \n'.format(f))
        return io.imread(f)


def load_bil_data(dataset_info, name):
    
    ''' 
    This panel provides a tool for load pre-determined datasets from BIL
    data currently available via https://download.brainimagelibrary.org/
    
    Current datasets are fMOST modality which included multi-resolution single-color
    projections.
    '''

    bilData = dataset_info['url']
    supported_file_types = ['tif', 'tiff', 'jp2']

    data = []
    for data_url in bilData:
        for ext in supported_file_types:
            images = sorted(getFilesHttp(data_url, ext))
            if len(images):
                images = [fsspec.open(x,'rb') for x in images]
                data.append(images)
    
    for idx, url_files in enumerate(data):
        if url_files[0].path.endswith('.tif') or url_files[0].path.endswith('.tiff'):
            store = tifffile.imread(url_files[0], aszarr=True)
            first_img = da.from_zarr(store)
        else:
            first_img = getImage(url_files[0])
        images = [delayed(getImage)(x) for x in url_files]
        images = [da.from_delayed(x, first_img.shape, dtype=first_img.dtype) for x in images]
        images = da.stack(images)
        data[idx] = images

    scale = dataset_info['scale']
    multiscale = True if len(dataset_info['url']) > 1 else False
    contrast_limits = dataset_info['contrast_limits']
    data = data if len(data)>1 else data[0]
    
    meta = {
        'name':name,
        'scale':scale,
        'multiscale':multiscale,
        'contrast_limits':contrast_limits
        # 'channel_axis':meta['name'][cc],
        # 'metadata':meta['metadata'],
        
        }

    return (data,meta,'image')


def load_single_image(dataset_info, name):
    image = dataset_info['url'][0]
    image = fsspec.open(image, 'rb')
    if image.path.endswith('.tif') or image.path.endswith('.tiff'):
        data = getImage(image)
    else:
        data = None
    meta = {
        'name': name,
        'scale': dataset_info['scale'],
        'multiscale': False,
        'contrast_limits': dataset_info['contrast_limits']
    }
    return data, meta, 'image'


class BILInfoHbox(QHBoxLayout):
    def __init__(self):
        super().__init__()
        logo = abspath(__file__, "resources/bil_logo.png")
        bil_logo_label = QLabel(f'<img src="{logo}" width="100" height="75">')
        bil_info_label = QLabel('<h2>Brain Image Library</h2> <a href="https://brainimagelibrary.org" style="color:gray;">brainimagelibrary.org</a>')
        bil_info_label.setOpenExternalLinks(True)
        self.addWidget(bil_logo_label)
        self.addWidget(bil_info_label)


class SpinnerLabel(QLabel):
    def __init__(self):
        super().__init__()
        spinner_movie = abspath(__file__, "resources/loading.gif")
        spinner = QMovie(spinner_movie)
        spinner.setScaledSize(QSize(50, 50))
        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
        self.setMovie(spinner)
        self.setHidden(True)


def load_bil_swc(url, dataset):
    from neurom import load_morphology
    import numpy as np

    response = requests.get(url)
    swc_data = response.text
    m = load_morphology(swc_data, 'swc')
    print("Morphology loaded")
    data = []
    for n in m.neurites:
        for section in n.iter_sections():
            pts = section.points[:, :3]
            pts_x = pts[:, 0].copy() / dataset["scale"][2]
            pts_y = pts[:, 1].copy() / dataset["scale"][1]
            pts_z = pts[:, 2].copy() / dataset["scale"][0]
            pts_rotated = np.empty_like(pts)
            pts_rotated[:, 0] = pts_z
            pts_rotated[:, 1] = pts_y
            pts_rotated[:, 2] = pts_x
            data.append(pts_rotated)
    meta = {
        "shape_type": 'path',
        "edge_width": 8,
        "edge_color": 'red',
        "scale": [dataset["scale"][0], dataset["scale"][1], dataset["scale"][2]],
        "name": "neuron tracings"
    }

    center_x, center_y, center_z = m.soma.center
    center_x /= dataset["scale"][2]
    center_y /= dataset["scale"][1]
    center_z /= dataset["scale"][0]
    soma = [center_z, center_y, center_x]

    soma_meta = {
        "face_color": "yellow",
        "edge_color": "black",
        "size": 200,
        "scale": [dataset["scale"][0], dataset["scale"][1], dataset["scale"][2]],
        "name": "soma"
    }

    paths_tuple = (data, meta, 'shapes')
    soma_tuple = (soma, soma_meta, 'points')
    print("Layer data ready. Rendering...")
    return soma_tuple, paths_tuple


def get_next_color():
    for color in color_map.colors[1:]:
        yield color


color_generator = get_next_color()


def abspath(root, relpath):
    """
    Credit to stardist-napari plugin
    """
    from pathlib import Path
    root = Path(root)
    if root.is_dir():
        path = root/relpath
    else:
        path = root.parent/relpath
    return str(path.absolute())


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [LoadCuratedDatasets, LoadImageStackFromURL, LoadMultiscaleDataFromURL, LoadNeuronMorphologyFromURL, LayerScaleControls, LoadHistologyImageFromURL]
