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
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit


class LoadBilData(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        self.datasets = sorted([key for key in get_datasets()])
        self.dataset = self.datasets[0] if len(self.datasets) else None
        self.swc_url = ""
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
        self.setLayout(vbox)

        # connect signals and slots
        load_button.clicked.connect(self.load_dataset)
        show_swc_button.clicked.connect(self.load_swc)

    def load_dataset(self):
        data, meta, layer_type = load_bil_data(self.dataset)
        print("meta", meta)
        self.viewer.add_image(data, **meta)

    def on_combobox_changed(self, value):
        self.dataset = value

    def load_swc(self):
        data, meta, layer_type = load_bil_swc(self.swc_url, self.dataset)
        self.viewer.add_shapes(data, **meta)

    def on_swc_url_changed(self, value):
        self.swc_url = value


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

    def getFilesHttp(url: str,ext: str) -> list:
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
            pts_x = pts[:, 0].copy() / dataset["scale"][1]
            pts_y = pts[:, 1].copy() / dataset["scale"][2]
            pts_z = pts[:, 2].copy() / dataset["scale"][0]
            pts_rotated = np.empty_like(pts)
            pts_rotated[:, 0] = pts_z
            pts_rotated[:, 1] = pts_y
            pts_rotated[:, 2] = pts_x
            data.append(pts_rotated)
    meta = {
        "shape_type": 'path',
        "edge_width": 4,
        "edge_color": 'red',
        "scale": [dataset["scale"][0], dataset["scale"][1], dataset["scale"][2]]
    }
    return (data, meta, 'shapes')


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return LoadBilData
