# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:49:37 2021

@author: alpha
"""

import napari, os
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
# from .h5layer import layerH5
import dask.array as da
from napari.layers import Image
from .dataset_info import get_datasets

import fsspec, requests
from bs4 import BeautifulSoup
from skimage import io
from dask import delayed
# import numpy as np

@magic_factory(auto_call=False,call_button="Load Dataset",
                dataset={"choices": [key for key in get_datasets()]}
                )



def load_bil_data(
    # viewer: napari.Viewer,
    dataset: str
) -> 'napari.types.LayerDataTuple':
    
    ''' 
    This panel provides a tool for load pre-determined datasets from BIL
    data currently available via http
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
    
        sampleImage = getImage(images[0])
    
        images = [delayed(getImage)(x) for x in images]
        images = [da.from_delayed(x, sampleImage.shape,dtype=sampleImage.dtype) for x in images]
        images = da.stack(images)
        data.append(images)
    
    
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
        
        
        
    # napari.view_image(images, meta=meta)
        
    
    return (data,meta,'image')

    # # napari.view_image(images, metadata={'scale':(100,3.5,3.5)})
    # napari.view_image(images, name=bilData.split('/')[-2],scale=(100.0,3.5,3.5))
    


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return load_bil_data

