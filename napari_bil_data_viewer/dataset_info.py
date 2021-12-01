# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:20:11 2021

@author: alpha
"""

def get_datasets():
    
    '''
    Dataset dict should be structured as:
        key = dataset_ID
        dict = {
            url: list of STR in decending resolution order
            scale: tuple (z,y,x) of the highest resolution level
            contrast_limits: list of int signifying low and high for 16 bit [0, 65535]
            } 
    '''
    
    datasets = {
        '2bdaf9e66a246844_multi':{
            'url':[
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1/',
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        
        '2bdaf9e66a246844':{
            'url':['https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_3.5_100um/'],
            'scale':(100,3.5,3.5),
            'contrast_limits':[0,65535]
            }
        
        
        }
        
        
        
    
    return datasets
    