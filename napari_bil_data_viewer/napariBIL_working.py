# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:08:10 2021

@author: alpha
"""

'''
View BIL data using napari

requires:
    Napari[all]
    requests
    bs4
    dask
    skimage
'''

import fsspec, requests
from bs4 import BeautifulSoup
from skimage import io
import dask.array as da
from dask import delayed
# import numpy as np
import napari

bilData = 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_3.5_100um/'
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

images = sorted(getFilesHttp(bilData, ext))
images = [fsspec.open(x,'rb') for x in images]

sampleImage = getImage(images[0])

images = [delayed(getImage)(x) for x in images]
images = [da.from_delayed(x, sampleImage.shape,dtype=sampleImage.dtype) for x in images]
images = da.stack(images)

# napari.view_image(images, metadata={'scale':(100,3.5,3.5)})
napari.view_image(images, name=bilData.split('/')[-2],scale=(100.0,3.5,3.5))


