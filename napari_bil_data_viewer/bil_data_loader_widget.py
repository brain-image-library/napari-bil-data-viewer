# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:49:37 2021

@author: alpha
"""

import napari
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
import dask.array as da
# from napari.layers import Image
import fsspec, requests
from bs4 import BeautifulSoup
from skimage import io
from dask import delayed
from .dataset_info import get_datasets
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit, QCheckBox


class LoadBilData(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.soma_layer = None
        self.tracings_layer = None
        self.datasets = sorted([key for key in get_datasets()])
        self.dataset = self.datasets[0] if len(self.datasets) else None
        self.swc_url = ""
        self.visualized_tracings = []
        self.neuron_sections = []
        self.init_ui()

    def init_ui(self):
        # create widgets
        dataset_label = QLabel("Select Dataset:")
        dataset_dropdown = QComboBox()
        dataset_dropdown.addItems(self.datasets)
        dataset_dropdown.currentTextChanged.connect(self.on_combobox_changed)
        load_button = QPushButton("Load Dataset")
        visualize_label = QLabel("Visualize SWC:")
        url_input = QLineEdit()
        url_input.setPlaceholderText("paste URL")
        url_input.textChanged.connect(self.on_swc_url_changed)
        show_swc_button = QPushButton("Show SWC")
        swc_checkboxes = []

        # create layout
        hbox0 = QHBoxLayout()
        hbox0.addWidget(dataset_label)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(dataset_dropdown)
        hbox1.addWidget(load_button)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(visualize_label)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(url_input)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(show_swc_button)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        # dynamically add checkboxes for SWC files
        dataset_dropdown.currentIndexChanged.connect(lambda: self.create_swc_checkboxes(dataset_dropdown.currentText(), vbox, swc_checkboxes))

        self.setLayout(vbox)

        # connect signals and slots
        load_button.clicked.connect(self.load_dataset)
        # show_swc_button.clicked.connect(self.load_swc)
        show_swc_button.clicked.connect(lambda: self.add_checkboxes(vbox, url_input.text(), swc_checkboxes))

    def load_dataset(self):
        data, meta, layer_type = load_bil_data(self.dataset)
        print("meta", meta)
        self.viewer.add_image(data, **meta)

    def on_combobox_changed(self, value):
        self.dataset = value

    def load_swc(self, url=None):
        import numpy as np
        from napari.utils.colormaps.colormap_utils import _color_random

        if not url:
            url = self.swc_url

        points, shapes = load_bil_swc(url, self.dataset)
        data, meta, __ = shapes
        self.neuron_sections.append(len(data))
        soma, soma_meta, __ = points
        random_color = _color_random(1, seed=np.random.uniform())
        meta["edge_color"] = random_color
        if self.tracings_layer:
            self.tracings_layer.add_paths(data, edge_color=random_color)
        else:
            self.tracings_layer = self.viewer.add_shapes(data, **meta)
        if self.soma_layer:
            self.soma_layer.add(soma)
        else:
            self.soma_layer = self.viewer.add_points(soma, **soma_meta)
        self.visualized_tracings.append(url)

    def on_swc_url_changed(self, value):
        self.swc_url = value

    def create_swc_checkboxes(self, dataset_name, vbox, swc_checkboxes):
        # remove existing checkboxes
        for checkbox in swc_checkboxes:
            vbox.removeWidget(checkbox)
            checkbox.setParent(None)

        # get SWC files for selected dataset
        swc_files = get_swc_files(dataset_name)

        # create checkboxes for each SWC file
        for swc_file in swc_files:
            checkbox = QCheckBox(swc_file)
            vbox.addWidget(checkbox)
            swc_checkboxes.append(checkbox)
            checkbox.stateChanged.connect(lambda state, path=swc_file: self.visualize_swc(path, state))

    def visualize_swc(self, path_to_swc, state):
        print("state", state)
        if state == Qt.Checked:
            print(f"Visualizing {path_to_swc}")
            self.load_swc(path_to_swc)
        else:
            print(f"Hiding {path_to_swc}")
            self.hide_swc(path_to_swc)

    def add_checkbox(self, vbox, swc_file_path, swc_checkboxes):
        if swc_file_path:
            checkbox = QCheckBox(swc_file_path)
            checkbox.setChecked(True)
            vbox.addWidget(checkbox)
            checkbox.stateChanged.connect(lambda state, path=swc_file_path: self.visualize_swc(path, state))
            swc_checkboxes.append(checkbox)
            self.load_swc(swc_file_path)

    def add_checkboxes(self, vbox, url, swc_checkboxes):
        # Check if the URL leads to a folder or a file
        if url.endswith('.swc'):
            self.add_checkbox(vbox, url, swc_checkboxes)
        else:
            # assume folder with swc
            swc_files = getFilesHttp(url, 'swc')
            print("swc files", swc_files)
            self.add_folder_checkboxes(vbox, swc_files, swc_checkboxes)

    def add_folder_checkboxes(self, vbox, swc_files, swc_checkboxes):
        # add a checkbox for each SWC file
        for swc_file in swc_files:
            self.add_checkbox(vbox, swc_file, swc_checkboxes)

    def hide_swc(self, url):
        # print("self.visualized_tracings before", self.visualized_tracings)
        # print("self.neuron_sections before", self.neuron_sections)
        url_index = self.visualized_tracings.index(url)
        # print("url_index", url_index)
        self.soma_layer.selected_data = set([url_index])
        self.soma_layer.remove_selected()
        start_index = sum(self.neuron_sections[:url_index])
        end_index = start_index + self.neuron_sections[url_index]
        print(start_index, end_index)
        indices_to_hide = range(start_index, end_index)
        self.tracings_layer.selected_data = set(indices_to_hide)
        self.tracings_layer.remove_selected()
        self.visualized_tracings.pop(url_index)
        self.neuron_sections.pop(url_index)
        # print("self.visualized_tracings after", self.visualized_tracings)
        # print("self.neuron_sections after", self.neuron_sections)


def get_swc_files(dataset_name):
    datasets = get_datasets()
    swc_files = datasets[dataset_name].get('swc', [])
    print("SWC files", swc_files)
    return swc_files


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


def load_bil_data(
    # viewer: napari.Viewer,
    dataset: str
) -> 'napari.types.LayerDataTuple':
    
    ''' 
    This panel provides a tool for load pre-determined datasets from BIL
    data currently available via https://download.brainimagelibrary.org/
    
    Current datasets are fMOST modality which included multi-resolution single-color
    projections.
    '''
    
    dataset_info = get_datasets()[dataset]
    
    bilData = dataset_info['url']
    ext = 'tif'

    def getImage(fileObj):
        with fileObj as f:
            print('Reading {} \n'.format(f))
            return io.imread(f)

    
    data = []
    for ii in bilData:
        images = sorted(getFilesHttp(ii, ext))
        images = [fsspec.open(x,'rb') for x in images]
        data.append(images)
    
    

    for idx,ii in enumerate(data):
        sampleImage = getImage(ii[0])
        images = [delayed(getImage)(x) for x in ii]
        images = [da.from_delayed(x, sampleImage.shape,dtype=sampleImage.dtype) for x in images]
        images = da.stack(images)
        data[idx] = images
    
    
    
    name = dataset
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
    

def load_bil_swc(url, dataset):
    from neurom import load_morphology
    import numpy as np
    from .fMOST_datasets import datasets

    print("Dataset", dataset)
    dataset = datasets.get(dataset, get_datasets()[dataset])
    print("Dataset", dataset)
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
    return soma_tuple, paths_tuple


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return LoadBilData
