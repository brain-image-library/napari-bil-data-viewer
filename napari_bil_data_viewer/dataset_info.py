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
#        'TEST_FULL_RES_ONLY_mouseID_405429-182725':{
#            'url':[
#                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1'],
#            'scale':(100,0.35,0.35),
#            'contrast_limits':[0,65535]
#            },
        
        'mouseID_404421-182720':{
            'url':[
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH1',  # full res
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH2',  # full res
                'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH1_0.23_100um',
                'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH1_2.3_100um'],
            'scale':(100,0.23,0.23),
            'contrast_limits': [0, 300]
            },
        
        'mouseID_405429-182725':{
            'url':[
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH2',  # full res
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1',  # full res
               'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits': [0, 450]
            },
        
        'mouseID_418245-182727':{
            'url':[
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH1',  # full res
                # 'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH2',  # full res
                'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,450]
            },
        
        'mouseID_380471-191813':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 1000]
            },
        
        'mouseID_362188-191815':{
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH1',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 450]
            },
        
        'mouseID_380470-191812':{
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH1',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH2',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 450]
            },
        
        'mouseID_426124-191808':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 450]
            },
        
        'mouseID_439168-191807':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 800]
            },
        
        'mouseID_443055-191805':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 600]
            },
        
        'mouseID_383680-18463':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 800]
            },
        
        'mouseID_383128-18465':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/red',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/green',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/green/projection',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/green/projection_res'],
            'scale':(100,0.23,0.23),
            'contrast_limits':[0, 450]
            },
        
        'mouseID_431038-191804':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH1_0.35_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH1_3.5_100um'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0, 450]
            },
        
        'mouseID_381488-18464':{
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH1_0.23_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH1_2.3_100um'],
            'scale':(100,0.23,0.23),
            'contrast_limits':[0, 450]
            },
        
        'mouseID_423019-191803':{
            'url':[
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH1',  # full res
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH1_0.32_100um',
               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH1_3.2_100um'],
            'scale':(100,0.32,0.32),
            'contrast_limits':[0, 450]
            },

        'mouseID_373187-191817': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH1',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH2',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH1_3.5_100um'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0,  450]
        },

        'mouseID_377387-18466': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH1',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH1_0.23_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH1_2.3_100um'
            ],
            'scale': (100, 0.23, 0.23),
            'contrast_limits': [0,  450]
        },

        'mouseID_325875-17543': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/CH1',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/green',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/red',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/CH1_3.5_100um'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0,  450]
        },

        'mouseID_405426-182724': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH1',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH1_3.5_100um'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0,  450]
        },

        'mouseID_420489-191801': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH1',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH2',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH1_3.5_100um'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0,  450]
        },

        'mouseID_417571-182722': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH1',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH1_0.23_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH1_2.3_100um'
            ],
            'scale': (100, 0.23, 0.23),
            'contrast_limits': [0,  450]
        },

        'mouseID_417570-182721': {  # checked, works
            'url': [
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH2',  # full res
                # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH1',  # full res
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH1_0.35_100um',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH1_3.5_100um'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0,  450]
        },
        'mouseID_445241-211779': {  # checked, works
            'contrast_limits': [0,  600],
            'scale': (100, 0.35, 0.35),
            'url': [
                # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH1'  # full res
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH1_projection/projection_5um'
            ]
        },
        'mouseID_445243-211780': {  # checked, works
            'contrast_limits': [0,  1000],
            'scale': (100, 0.35, 0.35),
            'url': [
                # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH1',  # full res
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH1_projection/projection_5um'
            ]
        },
        'mouseID_467362-211782': {  # checked, works
            'contrast_limits': [0,  800],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH1_projection/projection_5um']},
        'mouseID_486478-196478': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH1',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH1_projection/projection_0.35_100um',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH1_projection/projection_5_100um']},
        'mouseID_494230-211775': {  # checked, works
            'contrast_limits': [0,  1000],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH1_projection/projection_5um']},
        'mouseID_497458-211786': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH1_projection/projection_5um']},
        'mouseID_497462-211787': {  # checked, works
            'contrast_limits': [0,  600],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH1_projection/projection_5um']},
        'mouseID_497520-211776': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH1_projection/projection_5um']},
        'mouseID_500861-211788': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH1_projection/projection_5um']},
        'mouseID_510498-211777': {  # checked, works
            'contrast_limits': [0,  800],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH1_projection/projection_5um']},
        'mouseID_510502-211778': {  # checked, works
            'contrast_limits': [0,  600],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH1_projection/projection_5um']},
        'mouseID_522151-211806': {  # checked, works
            'contrast_limits': [0,  800],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH1_projection/projection_5um']},
        'mouseID_522152-211807': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH1_projection/projection_5um']},
        'mouseID_586838-211801': {  # checked, works
            'contrast_limits': [0,  300],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH1_projection/projection_5um']},
        'mouseID_586840-211802': {  # checked, works
            'contrast_limits': [0,  300],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH1_projection/projection_5um']},
        'mouseID_588922-211800': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH1_projection/projection_5um']},
        'mouseID_588923-211799': {  # checked, works
            'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH1',  # full res
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH1_projection/projection_5um']},

         # 'mouseID_210254-15257': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_210254-15257/Green',   # full res
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_210254-15257/Red'  # full res
         #                          ]
         #                          },
         'mouseID_360835-18049': {
                                  'contrast_limits': [0, 370],
                                  'scale': (100, 0.23, 0.23),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Green',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Green/projection',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Green/projection_res',
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Red',   # full res
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Red/projection',
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Red/projection_res'
                                  ]
                                  },
         'mouseID_362191-191816': {'contrast_limits': [0, 570],
                                   'scale': (100, 0.35, 0.35),
                                   'url': [
                                       # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362191-191816/CH2',  # full res
                                       # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362191-191816/CH1',  # full res
                                       'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362191-191816/CH1_0.35_100um',
                                       'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362191-191816/CH1_3.5_100um',
                                   ]
                                   },
         'mouseID_367667-18052': {'contrast_limits': [0, 400],
                                  'scale': (100, 0.23, 0.23),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_367667-18052/Green',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_367667-18052/Green/projection',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_367667-18052/Green/projection_res',
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_367667-18052/Red',  # full res
                                  ]
                                  },
         'mouseID_373641-18462': {'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373641-18462/CH2',  # full res
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373641-18462/CH1',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373641-18462/CH1_0.35_100um',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373641-18462/CH1_3.5_100um',
                                  ]
                                  },
         'mouseID_374706-18461': {'contrast_limits': [0,  450],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374706-18461/CH2',  # full res
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374706-18461/CH1',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374706-18461/CH1_0.35_100um',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374706-18461/CH1_3.5_100um',
                                  ]
                                  },
         'mouseID_374707-18452': {'contrast_limits': [0, 400],
                                  'scale': (100, 0.23, 0.23),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374707-18452/Green',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374707-18452/Green/projection',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374707-18452/Green/projection_res',
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374707-18452/Red'  # full res
                                  ]
                                  },
         # 'mouseID_375394-18468': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Green',  # full res
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Green/projection_100',
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Green/projection',
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Red',  # full res
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Red/projection_100',
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Red/projection'
         #                          ]
         #                          },
         # 'mouseID_378667-18469': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Green',  # full res
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Green/projection_100',
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Green/projection',
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Red',  # full res
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Red/projection_100',
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Red/projection']},
         # 'mouseID_378668-18470': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Green',  # full res
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Green/projection',
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Green/projection_100',
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Red',  # full res
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Red/projection',
         #                              'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Red/projection_100']},
         'mouseID_381487-18458': {'contrast_limits': [0, 600],
                                  'scale': (100, 0.23, 0.23),
                                  'url': [
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381487-18458/green',  # full res
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381487-18458/green/projection',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381487-18458/green/projection_res'
                                      # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381487-18458/red',  # full res
                                  ]
                                  },
         # 'mouseID_394528-18867': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_394528-18867/green'  # full res
         #                          ]
         #                          },
         'mouseID_411732-182718': {'contrast_limits': [0,  450],
                                   'scale': (100, 0.35, 0.35),
                                   'url': [
                                       # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_411732-182718/CH1',  # full res
                                       # 'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_411732-182718/CH2',  # full res
                                       'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_411732-182718/CH1_0.35_100um',
                                       'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_411732-182718/CH1_3.5_100um',
                                   ]
                                   },
        # '321237-17302': {'contrast_limits': [0,  450],
        #                   'scale': [],
        #                   'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321237-17302/green',
        #                           'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321237-17302/red']},
        #  '321244-17545': {'contrast_limits': [0,  450],
        #                   'scale': [],
        #                   'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321244-17545/green',
        #                           'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321244-17545/red']},
        #  '326952-17304': {'contrast_limits': [0,  450],
        #                   'scale': [],
        #                   'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/326952-17304/green',
        #                           'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/326952-17304/red']},
        #  '339951-17781': {'contrast_limits': [0,  450],
        #                   'scale': [],
        #                   'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/339951-17781/green',
        #                           'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/339951-17781/red']},
         '339952-17782': {'contrast_limits': [0, 600],
                          'scale': (100, 0.2, 0.2),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/339952-17782/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/339952-17782/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/339952-17782/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/339952-17782/red'   # full_res
                          ]},
         '351327-17787': {'contrast_limits': [0, 400],
                          'scale': (100, 0.23, 0.23),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351327-17787/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351327-17787/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351327-17787/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351327-17787/red'   # full_res
                          ]},
         '351331-17788': {'contrast_limits': [0, 400],
                          'scale': (100, 0.23, 0.23),
                          'url': [
                              # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351331-17788/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351331-17788/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351331-17788/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351331-17788/red'    # full_res
                          ]},
         '355458-18053': {'contrast_limits': [0, 200],
                          'scale': (100, 0.23, 0.23),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355458-18053/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355458-18053/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355458-18053/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355458-18053/red'   # full_res
                          ]},
         '355459-18054': {'contrast_limits': [0, 400],
                          'scale': (100, 0.35, 0.35),
                          'url': [
                              # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/red',   # full_res
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/red/projection',
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/red/projection_res'
                          ]},
         '358361-18047': {'contrast_limits': [0, 200],
                          'scale': (100, 0.35, 0.23),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/red',   # full_res
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/red/projection',
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/red/projection_res'
                          ]},
         '373367-18454': {'contrast_limits': [0, 1500],
                          'scale': (100, 0.23, 0.23),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373367-18454/green',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373367-18454/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373367-18454/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373367-18454/red'
                          ]},
         '373368-18455': {'contrast_limits': [0, 1500],
                          'scale': (100, 0.23, 0.23),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373368-18455/green',   # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373368-18455/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373368-18455/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373368-18455/red'   # full_res
                          ]},
         '381484-18457': {'contrast_limits': [0, 700],
                          'scale': (100, 0.23, 0.23),
                          'url': [
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/381484-18457/green',    # full_res
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/381484-18457/green/projection',
                                  'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/381484-18457/green/projection_res'
                                  # 'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/381484-18457/red'    # full_res
                          ]},
         '182683': {'contrast_limits': [0,  450],
                              'scale': (100, 0.35, 0.35),
                              'url': [
                                  # 'https://download.brainimagelibrary.org/ec/d7/ecd76000aad716f8/182683/182683/CH1',
                                  'https://download.brainimagelibrary.org/ec/d7/ecd76000aad716f8/182683/182683/CH1_0.35_100um',
                                  'https://download.brainimagelibrary.org/ec/d7/ecd76000aad716f8/182683/182683/CH1_3.5_100um'
                                  # 'https://download.brainimagelibrary.org/ec/d7/ecd76000aad716f8/182683/182683/CH2'
                              ]},
         'mouseID_18011710-18066': {'contrast_limits': [0,  450],
                                    'scale': (100, 5, 5),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/df/8d/df8d3922f971e331/mouseID_18011710-18066/CH1',
                                        # 'https://download.brainimagelibrary.org/df/8d/df8d3922f971e331/mouseID_18011710-18066/CH1_projection/projection_0.230um',  # TODO causes GL_MAX_TEXTURE_SIZE=32768 error
                                        'https://download.brainimagelibrary.org/df/8d/df8d3922f971e331/mouseID_18011710-18066/CH1_projection/projection_5um']},
         'mouseID_18011809-18072': {'contrast_limits': [0,  1200],
                                    'scale': (100, 5, 5),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/73/ec/73ec63a56c799b6a/mouseID_18011809-18072/CH1',
                                        # 'https://download.brainimagelibrary.org/73/ec/73ec63a56c799b6a/mouseID_18011809-18072/CH1_projection/projection_0.350um',  # TODO causes GL_MAX_TEXTURE_SIZE=32768 error
                                        'https://download.brainimagelibrary.org/73/ec/73ec63a56c799b6a/mouseID_18011809-18072/CH1_projection/projection_5um']},
         'mouseID_18011810-18073': {'contrast_limits': [0,  450],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/2f/f9/2ff927b79ce7c247/mouseID_18011810-18073/18073',
                                        # 'https://download.brainimagelibrary.org/2f/f9/2ff927b79ce7c247/mouseID_18011810-18073/18073/CH1_projection',
                                        # 'https://download.brainimagelibrary.org/2f/f9/2ff927b79ce7c247/mouseID_18011810-18073/CH1',
                                        'https://download.brainimagelibrary.org/2f/f9/2ff927b79ce7c247/mouseID_18011810-18073/CH1_projection/projection_0.350um',
                                        'https://download.brainimagelibrary.org/2f/f9/2ff927b79ce7c247/mouseID_18011810-18073/CH1_projection/projection_5um']},
         'mouseID_18082503-18965': {
                                    'contrast_limits': [0, 600],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/6d/b5/6db5ad6bbb46afcb/mouseID_18082503-18965/CH1',  # full res
                                        'https://download.brainimagelibrary.org/6d/b5/6db5ad6bbb46afcb/mouseID_18082503-18965/CH1_Projection',
                                        'https://download.brainimagelibrary.org/6d/b5/6db5ad6bbb46afcb/mouseID_18082503-18965/CH1_resample_Projection'
                                    ]
                                    },
         'mouseID_18082506-18968': {'contrast_limits': [0,  450],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/49/02/4902417b7c636fcc/mouseID_18082506-18968/CH1',  # full res
                                        'https://download.brainimagelibrary.org/49/02/4902417b7c636fcc/mouseID_18082506-18968/CH1_projection/projection_0.350um',
                                        'https://download.brainimagelibrary.org/49/02/4902417b7c636fcc/mouseID_18082506-18968/CH1_projection/projection_5um']},
         'mouseID_18082513-18975': {'contrast_limits': [0, 400],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/cf/6c/cf6cbb30bd18f3ad/mouseID_18082513-18975/CH1',   # full res
                                        'https://download.brainimagelibrary.org/cf/6c/cf6cbb30bd18f3ad/mouseID_18082513-18975/CH1_Projection',
                                        'https://download.brainimagelibrary.org/cf/6c/cf6cbb30bd18f3ad/mouseID_18082513-18975/CH1_resample_Projection'
                                    ]
                                    },
         'mouseID_18082518-18980': {'contrast_limits': [0, 800],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/05/79/057964871bc6ecfb/mouseID_18082518-18980/CH1',   # full res
                                        'https://download.brainimagelibrary.org/05/79/057964871bc6ecfb/mouseID_18082518-18980/CH1_Projection',
                                        'https://download.brainimagelibrary.org/05/79/057964871bc6ecfb/mouseID_18082518-18980/CH1_resample_Projection'
                                    ]
                                    },
         'mouseID_18082519-18981': {
                                    'contrast_limits': [0, 400],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/20/e9/20e90875c9ae4542/mouseID_18082519-18981/CH1',  # full res
                                        'https://download.brainimagelibrary.org/20/e9/20e90875c9ae4542/mouseID_18082519-18981/CH1_Projection',
                                        'https://download.brainimagelibrary.org/20/e9/20e90875c9ae4542/mouseID_18082519-18981/CH1_resample_Projection'
                                    ]
                                    },
         'mouseID_18101517-182280': {'contrast_limits': [0,  1000],
                                     'scale': (100, 5, 5),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/69/19/6919a5da8261ea78/mouseID_18101517-182280/CH1',  # full res
                                         # 'https://download.brainimagelibrary.org/69/19/6919a5da8261ea78/mouseID_18101517-182280/CH1_projection/projection_0.35_100um',  # TODO GL_MAX_TEXTURE_SIZE=32768
                                         'https://download.brainimagelibrary.org/69/19/6919a5da8261ea78/mouseID_18101517-182280/CH1_projection/projection_5_100um']},
         'mouseID_18103003-182051': {'contrast_limits': [0,  30],
                                     'scale': (50, 5, 5),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/e9/a2/e9a2af1aaa175f9b/mouseID_18103003-182051/182051',
                                         # 'https://download.brainimagelibrary.org/e9/a2/e9a2af1aaa175f9b/mouseID_18103003-182051/182051/CH1_projection',
                                         # 'https://download.brainimagelibrary.org/e9/a2/e9a2af1aaa175f9b/mouseID_18103003-182051/CH1',
                                         # 'https://download.brainimagelibrary.org/e9/a2/e9a2af1aaa175f9b/mouseID_18103003-182051/CH1_projection/projection_0.32_50um',  # TODO GL_MAX_TEXTURE_SIZE=32768
                                         'https://download.brainimagelibrary.org/e9/a2/e9a2af1aaa175f9b/mouseID_18103003-182051/CH1_projection/projection_5_50um']},
         'mouseID_18103012-182056': {'contrast_limits': [0,  35],
                                     'scale': (50, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/21/7f/217f83338fcc1632/mouseID_18103012-182056/182056',
                                         # 'https://download.brainimagelibrary.org/21/7f/217f83338fcc1632/mouseID_18103012-182056/182056/CH1_projection',
                                         # 'https://download.brainimagelibrary.org/21/7f/217f83338fcc1632/mouseID_18103012-182056/CH1',
                                         'https://download.brainimagelibrary.org/21/7f/217f83338fcc1632/mouseID_18103012-182056/CH1_projection/projection_0.32_50um',
                                         'https://download.brainimagelibrary.org/21/7f/217f83338fcc1632/mouseID_18103012-182056/CH1_projection/projection_5_50um']},
         'mouseID_18110102-182061': {'contrast_limits': [0,  35],
                                     'scale': (50, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/16/a5/16a50e365f275fc2/mouseID_18110102-182061/182061',
                                         # 'https://download.brainimagelibrary.org/16/a5/16a50e365f275fc2/mouseID_18110102-182061/182061/CH1_projection',
                                         # 'https://download.brainimagelibrary.org/16/a5/16a50e365f275fc2/mouseID_18110102-182061/CH1',
                                         'https://download.brainimagelibrary.org/16/a5/16a50e365f275fc2/mouseID_18110102-182061/CH1_projection/projection_0.32_50um',
                                         'https://download.brainimagelibrary.org/16/a5/16a50e365f275fc2/mouseID_18110102-182061/CH1_projection/projection_5_50um']},
         'mouseID_18110103-182062': {'contrast_limits': [0,  35],
                                     'scale': (50, 5, 5),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/55/50/555003a95bda40ec/mouseID_18110103-182062/CH1',  # full res
                                         # 'https://download.brainimagelibrary.org/55/50/555003a95bda40ec/mouseID_18110103-182062/CH1_projection/projection_0.32_50um',  # TODO GL_MAX_TEXTURE_SIZE=32768
                                         'https://download.brainimagelibrary.org/55/50/555003a95bda40ec/mouseID_18110103-182062/CH1_projection/projection_5_50um']},
         'mouseID_18110108-182065': {'contrast_limits': [0,  35],
                                     'scale': (50, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/11/63/1163b556224cc1e6/mouseID_18110108-182065/CH1',  # full res
                                         'https://download.brainimagelibrary.org/11/63/1163b556224cc1e6/mouseID_18110108-182065/CH1_projection/projection_0.32_50um',
                                         'https://download.brainimagelibrary.org/11/63/1163b556224cc1e6/mouseID_18110108-182065/CH1_projection/projection_5_50um']},
         'mouseID_18110113-182069': {'contrast_limits': [0,  25],
                                     'scale': (50, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/07/51/0751d3f0a5bd672c/mouseID_18110113-182069/CH1',  # full res
                                         'https://download.brainimagelibrary.org/07/51/0751d3f0a5bd672c/mouseID_18110113-182069/CH1_projection/projection_0.32_50um',
                                         'https://download.brainimagelibrary.org/07/51/0751d3f0a5bd672c/mouseID_18110113-182069/CH1_projection/projection_5_50um']},
         'mouseID_18121215-182932': {'contrast_limits': [0,  300],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/2e/31/2e31d0b226c4de3e/mouseID_18121215-182932/CH1',  # full res
                                         'https://download.brainimagelibrary.org/2e/31/2e31d0b226c4de3e/mouseID_18121215-182932/CH1_projection/projection_0.35_100um',
                                         'https://download.brainimagelibrary.org/2e/31/2e31d0b226c4de3e/mouseID_18121215-182932/CH1_projection/projection_5_100um']},
         'mouseID_19112221-195401': {'contrast_limits': [0,  100],
                                     'scale': (100, 0.325, 0.325),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/8a/f0/8af04b5469e576a7/mouseID_19112221-195401/CH1',  # full res
                                         'https://download.brainimagelibrary.org/8a/f0/8af04b5469e576a7/mouseID_19112221-195401/CH1_projection/projection_0.325um',
                                         'https://download.brainimagelibrary.org/8a/f0/8af04b5469e576a7/mouseID_19112221-195401/CH1_projection/projection_5um']},
         # 'mouseID_236174': {'contrast_limits': [0,  450],
         #                    'scale': [],
         #                    'url': [
         #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_236174/Raw-part1',
         #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_236174/Raw-part2']},
         # 'mouseID_297974': {'contrast_limits': [0,  450],
         #                    'scale': [],
         #                    'url': [
         #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_297974/green',
         #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_297974/red']},
         # 'mouseID_314107': {'contrast_limits': [0,  450],
         #                    'scale': [],
         #                    'url': [
         #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_314107/green',
         #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_314107/red']},
         # 'mouseID_327010-17298': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': []},
         # 'mouseID_342870-17541': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_342870-17541/green',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_342870-17541/red']},
         # 'mouseID_344548-17542': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_344548-17542/green',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_344548-17542/red']},
         # 'mouseID_351325-17786': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Green',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Green/projection',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Green/projection_100',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Red',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Red/projection',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Red/projection_100']},
         # 'mouseID_369739-18459': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_369739-18459/green',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_369739-18459/red']},
         # 'mouseID_374712-18453': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_374712-18453/green']},
         # 'mouseID_396477-18869': {'contrast_limits': [0,  450],
         #                          'scale': [],
         #                          'url': [
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_396477-18869/green',
         #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_396477-18869/red']},
         'mouseID_unknown-181349': {'contrast_limits': [0,  450],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/6f/2c/6f2cea13d7d94efd/mouseID_unknown-181349/181349',
                                        # 'https://download.brainimagelibrary.org/6f/2c/6f2cea13d7d94efd/mouseID_unknown-181349/181349/CH1_projection',
                                        # 'https://download.brainimagelibrary.org/6f/2c/6f2cea13d7d94efd/mouseID_unknown-181349/CH1',
                                        'https://download.brainimagelibrary.org/6f/2c/6f2cea13d7d94efd/mouseID_unknown-181349/CH1_projection/projection_0.350um',
                                        'https://download.brainimagelibrary.org/6f/2c/6f2cea13d7d94efd/mouseID_unknown-181349/CH1_projection/projection_5um']},
        'mouseID_019081501-193388': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081501-193388/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081501-193388/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081501-193388/CH1_3.5_100um']},
         'mouseID_019081503-193374': {'contrast_limits': [0, 450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081503-193374/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081503-193374/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081503-193374/CH1_3.5_100um']},
         'mouseID_019081504-193375': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081504-193375/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081504-193375/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081504-193375/CH1_3.5_100um']},
         'mouseID_019081505-193376': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081505-193376/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081505-193376/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081505-193376/CH1_3.5_100um']},
         'mouseID_019081506-193377': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081506-193377/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081506-193377/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081506-193377/CH1_3.5_100um']},
         'mouseID_019081507-193378': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081507-193378/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081507-193378/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081507-193378/CH1_3.5_100um']},
         'mouseID_019081508-193379': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081508-193379/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081508-193379/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081508-193379/CH1_3.5_100um']},
         'mouseID_019081510-193381': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081510-193381/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081510-193381/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081510-193381/CH1_3.5_100um']},
         'mouseID_019081511-193382': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081511-193382/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081511-193382/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081511-193382/CH1_3.5_100um']},
         'mouseID_019081512-193383': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.23, 0.23),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081512-193383/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081512-193383/CH1_0.23_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081512-193383/CH1_2.3_100um']},
         'mouseID_019081513-193385': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081513-193385/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081513-193385/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081513-193385/CH1_3.5_100um']},
         'mouseID_019081514-193386': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081514-193386/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081514-193386/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081514-193386/CH1_3.5_100um']},
         'mouseID_019081515-193387': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081515-193387/CH1',  # full res
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081515-193387/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081515-193387/CH1_3.5_100um']},
         'mouseID_18082502-18964': {'contrast_limits': [0,  800],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/06/f4/06f4ef728fd23689/mouseID_18082502-18964/CH1',  # full res
                                        'https://download.brainimagelibrary.org/06/f4/06f4ef728fd23689/mouseID_18082502-18964/CH1_0.35_100um',
                                        'https://download.brainimagelibrary.org/06/f4/06f4ef728fd23689/mouseID_18082502-18964/CH1_3.5_100um']},
         'mouseID_18082511-18973': {'contrast_limits': [0,  1500],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/95/39/953951d23ff7dee2/mouseID_18082511-18973/CH1',  # full res
                                        'https://download.brainimagelibrary.org/95/39/953951d23ff7dee2/mouseID_18082511-18973/CH1_0.35_100um',
                                        'https://download.brainimagelibrary.org/95/39/953951d23ff7dee2/mouseID_18082511-18973/CH1_3.5_100um']},
         'mouseID_18082512-18974': {'contrast_limits': [0,  450],
                                    'scale': (100, 0.35, 0.35),
                                    'url': [
                                        # 'https://download.brainimagelibrary.org/94/27/9427ada8f2699b11/mouseID_18082512-18974/CH1',  # full res
                                        'https://download.brainimagelibrary.org/94/27/9427ada8f2699b11/mouseID_18082512-18974/CH1_0.35_100um',
                                        'https://download.brainimagelibrary.org/94/27/9427ada8f2699b11/mouseID_18082512-18974/CH1_3.5_100um']},
         'mouseID_18101512-182275': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/36/cd/36cd086800a14408/mouseID_18101512-182275/CH1',  # full res
                                         'https://download.brainimagelibrary.org/36/cd/36cd086800a14408/mouseID_18101512-182275/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/36/cd/36cd086800a14408/mouseID_18101512-182275/CH1_3.5_100um']},
         'mouseID_18101514-182278': {'contrast_limits': [0,  200],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/52/2d/522d38ee2fea3ff5/mouseID_18101514-182278/CH1',  # full res
                                         'https://download.brainimagelibrary.org/52/2d/522d38ee2fea3ff5/mouseID_18101514-182278/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/52/2d/522d38ee2fea3ff5/mouseID_18101514-182278/CH1_3.5_100um']},
         'mouseID_18112111-182448': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112111-182448/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112111-182448/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112111-182448/CH1_3.5_100um']},
         'mouseID_18112613-182680': {'contrast_limits': [0,  300],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112613-182680/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112613-182680/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112613-182680/CH1_3.5_100um']},
         'mouseID_18112614-182681': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112614-182681/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112614-182681/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112614-182681/CH1_3.5_100um']},
         'mouseID_18112615-182682': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112615-182682/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112615-182682/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112615-182682/CH1_3.5_100um']},
         'mouseID_18121216-182931': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18121216-182931/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18121216-182931/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18121216-182931/CH1_3.5_100um']},
         'mouseID_19010302-190132': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010302-190132/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010302-190132/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010302-190132/CH1_3.5_100um']},
         'mouseID_19010303-190134': {'contrast_limits': [0,  1000],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010303-190134/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010303-190134/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010303-190134/CH1_3.5_100um']},
         'mouseID_19010304-190133': {'contrast_limits': [0,  800],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010304-190133/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010304-190133/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010304-190133/CH1_3.5_100um']},
         'mouseID_19010305-190128': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010305-190128/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010305-190128/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010305-190128/CH1_3.5_100um']},
         'mouseID_19010306-190130': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010306-190130/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010306-190130/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010306-190130/CH1_3.5_100um']},
         'mouseID_19010307-190131': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010307-190131/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010307-190131/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010307-190131/CH1_3.5_100um']},
         'mouseID_19010308-190129': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010308-190129/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010308-190129/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010308-190129/CH1_3.5_100um']},
         'mouseID_19010309-190138': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010309-190138/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010309-190138/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010309-190138/CH1_3.5_100um']},
         'mouseID_19010310-190135': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010310-190135/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010310-190135/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010310-190135/CH1_3.5_100um']},
         'mouseID_19010312-190136': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010312-190136/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010312-190136/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010312-190136/CH1_3.5_100um']},
         'mouseID_19011801-190363': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011801-190363/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011801-190363/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011801-190363/CH1_3.5_100um']},
         'mouseID_19011802-190364': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.23, 0.23),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011802-190364/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011802-190364/CH1_0.23_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011802-190364/CH1_2.3_100um']},
         'mouseID_19011803-190365': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011803-190365/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011803-190365/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011803-190365/CH1_3.5_100um']},
         'mouseID_19011804-190366': {'contrast_limits': [0,  600],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011804-190366/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011804-190366/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011804-190366/CH1_3.5_100um']},
         'mouseID_19011805-190367': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011805-190367/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011805-190367/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011805-190367/CH1_3.5_100um']},
         'mouseID_19011806-190368': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011806-190368/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011806-190368/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011806-190368/CH1_3.5_100um']},
         'mouseID_19011807-190369': {'contrast_limits': [0,  800],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011807-190369/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011807-190369/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011807-190369/CH1_3.5_100um']},
         'mouseID_19011808-190370': {'contrast_limits': [0,  200],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011808-190370/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011808-190370/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011808-190370/CH1_3.5_100um']},
         'mouseID_19012101-190381': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/a2/6b/a26b3e1028ce1f09/mouseID_19012101-190381/CH1',  # full res
                                         'https://download.brainimagelibrary.org/a2/6b/a26b3e1028ce1f09/mouseID_19012101-190381/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/a2/6b/a26b3e1028ce1f09/mouseID_19012101-190381/CH1_3.5_100um']},
         'mouseID_19022512-190902': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022512-190902/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022512-190902/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022512-190902/CH1_3.5_100um']},
         'mouseID_19022513-190891': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022513-190891/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022513-190891/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022513-190891/CH1_3.5_100um']},
         'mouseID_19022514-190892': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.23, 0.23),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022514-190892/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022514-190892/CH1_0.23_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022514-190892/CH1_2.3_100um']},
         'mouseID_19022515-190900': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022515-190900/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022515-190900/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022515-190900/CH1_3.5_100um']},
         'mouseID_19022516-190901': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022516-190901/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022516-190901/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022516-190901/CH1_3.5_100um']},
         'mouseID_19022518_190903': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022518_190903/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022518_190903/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022518_190903/CH1_3.5_100um']},
         'mouseID_19022519-190905': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.23, 0.23),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022519-190905/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022519-190905/CH1_0.23_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022519-190905/CH1_2.3_100um']},
         'mouseID_19022520-190904': {'contrast_limits': [0,  200],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022520-190904/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022520-190904/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022520-190904/CH1_3.5_100um']},
         'mouseID_19022521-190896': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022521-190896/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022521-190896/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022521-190896/CH1_3.5_100um']},
         'mouseID_19022522-190895': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022522-190895/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022522-190895/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022522-190895/CH1_3.5_100um']},
         'mouseID_19022523-190893': {'contrast_limits': [0,  200],
                                     'scale': (100, 0.23, 0.23),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022523-190893/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022523-190893/CH1_0.23_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022523-190893/CH1_2.3_100um']},
         'mouseID_19022524-190894': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022524-190894/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022524-190894/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022524-190894/CH1_3.5_100um']},
         'mouseID_19022525-190897': {'contrast_limits': [0,  200],
                                     'scale': (100, 0.23, 0.23),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022525-190897/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022525-190897/CH1_0.23_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022525-190897/CH1_2.3_100um']},
         'mouseID_19022526-190898': {'contrast_limits': [0,  200],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022526-190898/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022526-190898/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022526-190898/CH1_3.5_100um']},
         'mouseID_19022714-190909': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022714-190909/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022714-190909/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022714-190909/CH1_3.5_100um']},
         'mouseID_19022715-190906': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022715-190906/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022715-190906/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022715-190906/CH1_3.5_100um']},
         'mouseID_19022716-190907': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022716-190907/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022716-190907/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022716-190907/CH1_3.5_100um']},
         'mouseID_19022717-190908': {'contrast_limits': [0,  300],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022717-190908/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022717-190908/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022717-190908/CH1_3.5_100um']},
         'mouseID_19030601-191223': {'contrast_limits': [0,  25],
                                     'scale': (100, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030601-191223/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030601-191223/CH1_0.32_50um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030601-191223/CH1_3.2_50um']},
         'mouseID_19030602-191224': {'contrast_limits': [0,  25],
                                     'scale': (100, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030602-191224/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030602-191224/CH1_0.32_50um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030602-191224/CH1_3.2_50um']},
         'mouseID_19030603-191225': {'contrast_limits': [0,  25],
                                     'scale': (100, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030603-191225/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030603-191225/CH1_0.32_50um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030603-191225/CH1_3.2_50um']},
         'mouseID_19030606-191227': {'contrast_limits': [0,  25],
                                     'scale': (100, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030606-191227/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030606-191227/CH1_0.32_50um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030606-191227/CH1_3.2_50um']},
         'mouseID_19030607-191192': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030607-191192/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030607-191192/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030607-191192/CH1_3.5_100um']},
         'mouseID_19030608-191193': {'contrast_limits': [0,  1500],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030608-191193/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030608-191193/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030608-191193/CH1_3.5_100um']},
         'mouseID_19030609-191194': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030609-191194/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030609-191194/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030609-191194/CH1_3.5_100um']},
         'mouseID_19030610-191195': {'contrast_limits': [0,  1000],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030610-191195/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030610-191195/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030610-191195/CH1_3.5_100um']},
         'mouseID_19030611-191196': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030611-191196/CH1',  # full res
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030611-191196/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030611-191196/CH1_3.5_100um']},
         'mouseID_19030612-191228': {'contrast_limits': [0,  20],
                                     'scale': (100, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030612-191228/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030612-191228/CH1_0.32_50um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030612-191228/CH1_3.2_50um']},
         'mouseID_19030613-191229': {'contrast_limits': [0,  20],
                                     'scale': (100, 0.32, 0.32),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030613-191229/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030613-191229/CH1_0.32_50um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030613-191229/CH1_3.2_50um']},
         'mouseID_19030614-191197': {'contrast_limits': [0,  600],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030614-191197/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030614-191197/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030614-191197/CH1_3.5_100um']},
         'mouseID_19030615-191198': {'contrast_limits': [0,  800],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030615-191198/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030615-191198/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030615-191198/CH1_3.5_100um']},
         'mouseID_19030616-191199': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030616-191199/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030616-191199/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030616-191199/CH1_3.5_100um']},
         'mouseID_19032503-191186': {'contrast_limits': [0,  1500],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032503-191186/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032503-191186/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032503-191186/CH1_3.5_100um']},
         'mouseID_19032504-191187': {'contrast_limits': [0,  1500],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032504-191187/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032504-191187/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032504-191187/CH1_3.5_100um']},
         'mouseID_19032505-191185': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032505-191185/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032505-191185/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032505-191185/CH1_3.5_100um']},
         'mouseID_19032506-191184': {'contrast_limits': [0,  600],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032506-191184/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032506-191184/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032506-191184/CH1_3.5_100um']},
         'mouseID_19032507-191175': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032507-191175/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032507-191175/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032507-191175/CH1_3.5_100um'
                                     ],
                                     },
         'mouseID_19032508-191171': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032508-191171/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032508-191171/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032508-191171/CH1_3.5_100um'
                                     ],
                                     },
         'mouseID_19032509-191174': {'contrast_limits': [0,  100],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032509-191174/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032509-191174/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032509-191174/CH1_3.5_100um']},
         'mouseID_19032510-191173': {'contrast_limits': [0,  300],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032510-191173/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032510-191173/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032510-191173/CH1_3.5_100um']},
         'mouseID_19032511-191176': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.23, 0.23),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032511-191176/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032511-191176/CH1_0.23_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032511-191176/CH1_2.3_100um']},
         'mouseID_19032514-191183': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032514-191183/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032514-191183/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032514-191183/CH1_3.5_100um']},
         'mouseID_19032515-191182': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032515-191182/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032515-191182/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032515-191182/CH1_3.5_100um']},
         'mouseID_19032516-191180': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032516-191180/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032516-191180/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032516-191180/CH1_3.5_100um']},
         'mouseID_19032517-191178': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032517-191178/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032517-191178/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032517-191178/CH1_3.5_100um']},
         'mouseID_19032518-191177': {'contrast_limits': [0,  100],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032518-191177/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032518-191177/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032518-191177/CH1_3.5_100um']},
         'mouseID_19032519-191179': {'contrast_limits': [0,  450],
                                     'scale': (100, 0.35, 0.35),
                                     'url': [
                                         # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032519-191179/CH1',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032519-191179/CH1_0.35_100um',
                                         'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032519-191179/CH1_3.5_100um']},
         'mouseID_463865-192341': {'contrast_limits': [0,  300],
                                   'scale': (100, 0.35, 0.35),
                                   'url': [
                                       # 'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_463865-192341/CH1',
                                       'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_463865-192341/CH1_0.35_100um',
                                       'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_463865-192341/CH1_3.5_100um',
                                       # 'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_463865-192341/CH2_10_10_10um'
                                   ]
                                   },
         'mouseID_w19051002-192869': {'contrast_limits': [0,  600],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051002-192869/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051002-192869/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051002-192869/CH1_3.5_100um']},
         'mouseID_w19051003-192868': {'contrast_limits': [0,  600],
                                      'scale': (100, 0.23, 0.23),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051003-192868/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051003-192868/CH1_0.23_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051003-192868/CH1_2.3_100um']},
         'mouseID_w19051004-192867': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051004-192867/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051004-192867/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051004-192867/CH1_3.5_100um']},
         'mouseID_w19051005-192870': {'contrast_limits': [0,  600],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051005-192870/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051005-192870/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051005-192870/CH1_3.5_100um']},
         'mouseID_w19051006-192865': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051006-192865/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051006-192865/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051006-192865/CH1_3.5_100um']},
         'mouseID_w19051007-192858': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051007-192858/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051007-192858/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051007-192858/CH1_3.5_100um']},
         'mouseID_w19051009-192860': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.23, 0.23),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051009-192860/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051009-192860/CH1_0.23_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051009-192860/CH1_2.3_100um']},
         'mouseID_w19051010-192861': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051010-192861/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051010-192861/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051010-192861/CH1_3.5_100um']},
         'mouseID_w19051011-192855': {'contrast_limits': [0,  800],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051011-192855/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051011-192855/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051011-192855/CH1_3.5_100um']},
         'mouseID_w19051012-192856': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051012-192856/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051012-192856/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051012-192856/CH1_3.5_100um']},
         'mouseID_w19051013-192862': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051013-192862/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051013-192862/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051013-192862/CH1_3.5_100um']},
         'mouseID_w19051015-192853': {'contrast_limits': [0,  350],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051015-192853/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051015-192853/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051015-192853/CH1_3.5_100um']},
         'mouseID_w19051017-192863': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.23, 0.23),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051017-192863/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051017-192863/CH1_0.23_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051017-192863/CH1_2.3_100um']},
         'mouseID_w19051020-192857': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051020-192857/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051020-192857/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051020-192857/CH1_3.5_100um']},
         'mouseID_w19082902-193644': {'contrast_limits': [0,  800],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082902-193644/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082902-193644/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082902-193644/CH1_3.5_100um']},
         'mouseID_w19082904-193646': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082904-193646/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082904-193646/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082904-193646/CH1_3.5_100um']},
         'mouseID_w19082905-193647': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.23, 0.23),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082905-193647/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082905-193647/CH1_0.23_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082905-193647/CH1_2.3_100um']},
         'mouseID_w19082908-193650': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.23, 0.23),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082908-193650/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082908-193650/CH1_0.23_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082908-193650/CH1_2.3_100um']},
         'mouseID_w19082909-193651': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082909-193651/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082909-193651/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082909-193651/CH1_3.5_100um']},
         'mouseID_w19082922-193663': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082922-193663/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082922-193663/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082922-193663/CH1_3.5_100um']},
         'mouseID_w19082925-193666': {'contrast_limits': [0,  600],
                                      'scale': (100, 0.35, 0.35),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082925-193666/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082925-193666/CH1_0.35_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082925-193666/CH1_3.5_100um']},
         'mouseID_w19091704-194089': {'contrast_limits': [0,  200],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091704-194089/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091704-194089/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091704-194089/CH1_3.2_100um']},
         'mouseID_w19091705-194090': {'contrast_limits': [0,  200],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091705-194090/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091705-194090/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091705-194090/CH1_3.2_100um']},
         'mouseID_w19091706-194091': {'contrast_limits': [0,  200],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091706-194091/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091706-194091/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091706-194091/CH1_3.2_100um']},
         'mouseID_w19091707-194092': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091707-194092/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091707-194092/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091707-194092/CH1_3.2_100um']},
         'mouseID_w19091708-194093': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091708-194093/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091708-194093/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091708-194093/CH1_3.2_100um']},
         'mouseID_w19091709-194094': {'contrast_limits': [0,  450],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091709-194094/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091709-194094/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091709-194094/CH1_3.2_100um']},
         'mouseID_w19091710-194095': {'contrast_limits': [0,  300],
                                      'scale': (100, 0.32, 0.32),
                                      'url': [
                                          # 'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091710-194095/CH1',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091710-194095/CH1_0.32_100um',
                                          'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091710-194095/CH1_3.2_100um']},
        '212083': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212083/CH1_projection/projection_0.325um',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212083/CH1_projection/projection_5um'
            ]
        },
        '212084': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212084/CH1_projection/projection_0.325um',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212084/CH1_projection/projection_5um'
            ]
        },
        '212085': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212085/CH1_projection/projection_0.325um',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212085/CH1_projection/projection_5um'
            ]
        },
        '212086': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212086/CH1_projection/projection_0.325um',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212086/CH1_projection/projection_5um'
            ]
        },
        '212087': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212087/CH1_projection/projection_0.325um',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212087/CH1_projection/projection_5um'
            ]
        },
        '211043': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211043/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211043/CH1_projection/projection_5um/'
            ]
        },
        '211044': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211044/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211044/CH1_projection/projection_5um/'
            ]
        },
        '211045': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211045/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211045/CH1_projection/projection_5um/'
            ]
        },
        '211046': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211046/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211046/CH1_projection/projection_5um/'
            ]
        },
        '211054': {
            'contrast_limits': [0, 100],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211054/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211054/CH1_projection/projection_5um/'
            ]
        },
        '211056': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211056/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211056/CH1_projection/projection_5um/'
            ]
        },
        '211060': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211060/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211060/CH1_projection/projection_5um/'
            ]
        },
        '211061': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211061/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/211061/CH1_projection/projection_5um/'
            ]
        },
        '212088': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212088/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212088/CH1_projection/projection_5um/'
            ]
        },
        '212089': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212089/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212089/CH1_projection/projection_5um/'
            ]
        },
        '212090': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212090/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212090/CH1_projection/projection_5um/'
            ]
        },
        '212091': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212091/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212091/CH1_projection/projection_5um/'
            ]
        },
        '212092': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212092/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212092/CH1_projection/projection_5um/'
            ]
        },
        '212094': {
            'contrast_limits': [0, 100],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212094/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/a9/3c/a93ce7c42b77aaf1/212094/CH1_projection/projection_5um/'
            ]
        },
        '220244': {
            'contrast_limits': [0, 300],
            'scale': (100, 5, 5),
            'url': [
                # 'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220244/CH1_projection/projection_0.325um/',  # TODO: GL_MAX_TEXTURE_SIZE=32768
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220244/CH1_projection/projection_5um/'
            ]
        },
        '220245': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220245/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220245/CH1_projection/projection_5um/'
            ]
        },
        '220246': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220246/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220246/CH1_projection/projection_5um/'
            ]
        },
        '220247': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220247/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220247/CH1_projection/projection_5um/'
            ]
        },
        '220248': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220248/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220248/CH1_projection/projection_5um/'
            ]
        },
        '220249': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220249/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220249/CH1_projection/projection_5um/'
            ]
        },
        '220250': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220250/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220250/CH1_projection/projection_5um/'
            ]
        },
        '220251': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220251/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220251/CH1_projection/projection_5um/'
            ]
        },
        '220252': {
            'contrast_limits': [0, 300],
            'scale': (100, 5, 5),
            'url': [
                # 'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220252/CH1_projection/projection_0.325um/',  # TODO GL_MAX_TEXTURE_SIZE=32768
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220252/CH1_projection/projection_5um/'
            ]
        },
        '220403': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220403/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220403/CH1_projection/projection_5um/'
            ]
        },
        '220404': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220404/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220404/CH1_projection/projection_5um/'
            ]
        },
        '220405': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220405/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220405/CH1_projection/projection_5um/'
            ]
        },
        '220406': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220406/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220406/CH1_projection/projection_5um/'
            ]
        },
        '220407': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220407/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220407/CH1_projection/projection_5um/'
            ]
        },
        '220408': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220408/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220408/CH1_projection/projection_5um/'
            ]
        },
        '220409': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220409/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220409/CH1_projection/projection_5um/'
            ]
        },
        '220410': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220410/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220410/CH1_projection/projection_5um/'
            ]
        },
        '220411': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220411/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220411/CH1_projection/projection_5um/'
            ]
        },
        '220412': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220412/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220412/CH1_projection/projection_5um/'
            ]
        },
        '220413': {
            'contrast_limits': [0, 300],
            'scale': (100, 5, 5),
            'url': [
                # 'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220413/CH1_projection/projection_0.325um/',  # TODO GL_MAX_TEXTURE_SIZE=32768
                'https://download.brainimagelibrary.org/d5/c6/d5c66aceb1458fa7/220413/CH1_projection/projection_5um/'
            ]
        },
        '212093': {
            'contrast_limits': [0, 100],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212093/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212093/CH1_projection/projection_5um/'
            ]
        },
        '212095': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212095/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212095/CH1_projection/projection_5um/'
            ]
        },
        '212096': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212096/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212096/CH1_projection/projection_5um/'
            ]
        },
        '212097': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212097/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212097/CH1_projection/projection_5um/'
            ]
        },
        '212098': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212098/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212098/CH1_projection/projection_5um/'
            ]
        },
        '212099': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212099/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212099/CH1_projection/projection_5um/'
            ]
        },
        '212100': {
            'contrast_limits': [0, 100],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212100/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212100/CH1_projection/projection_5um/'
            ]
        },
        '212102': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212102/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212102/CH1_projection/projection_5um/'
            ]
        },
        '212103': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212103/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212103/CH1_projection/projection_5um/'
            ]
        },
        '212104': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212104/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212104/CH1_projection/projection_5um/'
            ]
        },
        '212105': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212105/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/212105/CH1_projection/projection_5um/'
            ]
        },
        '220104': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220104/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220104/CH1_projection/projection_5um/'
            ]
        },
        '220105': {
            'contrast_limits': [0, 150],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220105/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220105/CH1_projection/projection_5um/'
            ]
        },
        '220106': {
            'contrast_limits': [0, 100],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220106/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220106/CH1_projection/projection_5um/'
            ]
        },
        '220107': {
            'contrast_limits': [0, 100],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220107/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220107/CH1_projection/projection_5um/'
            ]
        },
        '220108': {
            'contrast_limits': [0, 150],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220108/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220108/CH1_projection/projection_5um/'
            ]
        },
        '220109': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220109/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220109/CH1_projection/projection_5um/'
            ]
        },
        '220110': {
            'contrast_limits': [0, 150],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220110/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220110/CH1_projection/projection_5um/'
            ]
        },
        '220111': {
            'contrast_limits': [0, 150],
            'scale': (100, 0.325, 0.325),
            'url': [
                # 'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220111/CH1_projection/projection_0.325um/',  # TODO: GL_MAX_TEXTURE_SIZE 32768
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220111/CH1_projection/projection_5um/'
            ]
        },
        '220112': {
            'contrast_limits': [0, 150],
            'scale': (100, 0.325, 0.325),
            'url': [
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220112/CH1_projection/projection_0.325um/',
                'https://download.brainimagelibrary.org/7c/9c/7c9c8934ffd0bae5/220112/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_576273-211540': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_576273-211540/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_576273-211540/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_574889-211544': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_574889-211544/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_574889-211544/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_578438-211546': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_578438-211546/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_578438-211546/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_574872-211547': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_574872-211547/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_574872-211547/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_577639-211549': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_577639-211549/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_577639-211549/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_578169-211791': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_578169-211791/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_578169-211791/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_538071-211803': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_538071-211803/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_538071-211803/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_538073-211804': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_538073-211804/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_538073-211804/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_538074-211805': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_538074-211805/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_538074-211805/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_595750-220037': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_595750-220037/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_595750-220037/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_599374-220040': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_599374-220040/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_599374-220040/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_451347-211783': {
            'contrast_limits': [0, 600],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_451347-211783/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_451347-211783/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_451348-211784': {
            'contrast_limits': [0, 1000],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_451348-211784/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_451348-211784/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_597666-220039': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_597666-220039/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_597666-220039/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_590965-220032': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_590965-220032/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_590965-220032/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_590969-220034': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_590969-220034/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_590969-220034/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_591448-220031': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_591448-220031/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_591448-220031/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_588379-211798': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_588379-211798/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_588379-211798/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_599345-220042': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_599345-220042/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_599345-220042/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_599346-220043': {
            'contrast_limits': [0, 300],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_599346-220043/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_599346-220043/CH1_projection/projection_5um/'
            ]
        },
        'mouseID_591228-220030': {
            'contrast_limits': [0, 450],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_591228-220030/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/9a/ae/9aae87938026636d/mouseID_591228-220030/CH1_projection/projection_5um/'
            ]
        },

        #
        # 'mouseID_': {
        #     'url': [
        #         '',
        #         ''
        #     ],
        #     'scale': (),
        #     'contrast_limits': [0, 65535]
        # },
        
        }
        
        
        
    print("Total datasets:", len(datasets))
    return datasets
