# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:49:37 2021

@author: alpha
"""

import napari, os
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
# from .h5layer import layerH5
from .reader import ims_reader
import dask.array as da
from typing import List
from napari.layers import Image
from dataset_info import get_datasets

import fsspec, requests
from bs4 import BeautifulSoup
from skimage import io
import dask.array as da
from dask import delayed
# import numpy as np
import napari

@magic_factory(auto_call=False,call_button="Load Dataset",
                dataset={"choices": [key for key in get_datasets()]}
                )



def load_bil_data(
    viewer: napari.Viewer,
    dataset: str
) -> 'napari.types.LayerDataTuple':
    
    ''' 
    This panel provides a tool for load pre-determined datasets from BIL
    data currently available via http
    '''
    
    
    
    ## Load data for IMS file using the loader function
    for idx in viewer.layers:
        # print(viewer.layers[str(idx)].data)
        try:
            tupleOut = ims_reader(
                viewer.layers[str(idx)].metadata['fileName'],
                colorsIndependant=True,
                resLevel=lowest_resolution_level
                )
        except ValueError as e:
            print(e)
            return
        
        break
    '''tupleOut is a tuple for each channel in the ims file
    structured as: [ ( [listOfMultiscaleDataCh1],metaDataDict ), 
                   ( [listOfMultiscaleDataCh2],metaDataDict ) ]
    '''
    # print(tupleOut)
    
    ## Determine Channel Names extracted from IMS file
    channelNames = []
    for tt in tupleOut:
        channelNames.append(tt[1]['name'])
    # print(channelNames)
    
    # for idx in viewer.layers:
    #     print(viewer.layers[str(idx)].data)
    
    ## Collect viewer state info about each layer with the same names extracted 
    ## from the ims file.  Add these parameters to the metadata extracted from file.
    ## Then delete the old layers
    
    ## Force viewer into 2D mode to avoid interpolation and
    ## axes don't match errors.  Not sure why these are caused
    if viewer.dims.ndisplay == 3:
        viewer.dims.ndisplay = 2
        
    for num,idx in enumerate(channelNames):
        
        tmp = {
            'opacity':viewer.layers[str(idx)].opacity,
            'gamma':viewer.layers[str(idx)].gamma,
            'colormap':viewer.layers[str(idx)].colormap,
            'blending':viewer.layers[str(idx)].blending,
            'interpolation':viewer.layers[str(idx)].interpolation,
            'visible':viewer.layers[str(idx)].visible,
            'rendering':viewer.layers[str(idx)].rendering
            
            # 'contrast_limits_range':viewer.layers[str(idx)].contrast_limits
            
            }
        
        tupleOut[num][1].update(tmp)
        
        del(viewer.layers[str(idx)])

    ## Return the tuple data that will be loaded into the viewer
    return tupleOut

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return load_bil_data

