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
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH1_0.23_100um/',
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH1_2.3_100um/'],
            'scale':(100,0.23,0.23),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_405429-182725':{
            'url':[
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_418245-182727':{
            'url':[
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_380471-191813':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_362188-191815':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_380470-191812':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_426124-191808':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_439168-191807':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_443055-191805':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_383680-18463':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_383128-18465':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/green/projection/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/green/projection_res/'],
            'scale':(100,0.23,0.23),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_431038-191804':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH1_0.35_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH1_3.5_100um/'],
            'scale':(100,0.35,0.35),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_381488-18464':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH1_0.23_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH1_2.3_100um/'],
            'scale':(100,0.23,0.23),
            'contrast_limits':[0,65535]
            },
        
        'mouseID_423019-191803':{
            'url':[
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH1_0.32_100um/',
                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH1_3.2_100um/'],
            'scale':(100,0.32,0.32),
            'contrast_limits':[0,65535]
            },

        'mouseID_373187-191817': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH1_0.35_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH1_3.5_100um/'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0, 65535]
        },

        'mouseID_377387-18466': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH1_0.23_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH1_2.3_100um/'
            ],
            'scale': (100, 0.23, 0.23),
            'contrast_limits': [0, 65535]
        },

        'mouseID_325875-17543': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/CH1_0.35_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/CH1_3.5_100um/'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0, 65535]
        },

        'mouseID_405426-182724': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH1_0.35_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH1_3.5_100um/'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0, 65535]
        },

        'mouseID_420489-191801': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH1_0.35_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH1_3.5_100um/'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0, 65535]
        },

        'mouseID_417571-182722': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH1_0.23_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH1_2.3_100um/'
            ],
            'scale': (100, 0.23, 0.23),
            'contrast_limits': [0, 65535]
        },

        'mouseID_417570-182721': {  # checked, works
            'url': [
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH1_0.35_100um/',
                'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH1_3.5_100um/'
            ],
            'scale': (100, 0.35, 0.35),
            'contrast_limits': [0, 65535]
        },
        'mouseID_445241-211779': {  # checked, works
            'contrast_limits': [0, 65535],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH1_projection/projection_5um'
            ]
        },
        'mouseID_445243-211780': {  # checked, works
            'contrast_limits': [0, 65535],
            'scale': (100, 0.35, 0.35),
            'url': [
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH1_projection/projection_0.350um',
                'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH1_projection/projection_5um'
            ]
        },
        'mouseID_467362-211782': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH1_projection/projection_5um']},
        'mouseID_486478-196478': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH1_projection/projection_0.35_100um',
                                      'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH1_projection/projection_5_100um']},
        'mouseID_494230-211775': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH1_projection/projection_5um']},
        'mouseID_497458-211786': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH1_projection/projection_5um']},
        'mouseID_497462-211787': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH1_projection/projection_5um']},
        'mouseID_497520-211776': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH1_projection/projection_5um']},
        'mouseID_500861-211788': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH1_projection/projection_5um']},
        'mouseID_510498-211777': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH1_projection/projection_5um']},
        'mouseID_510502-211778': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH1_projection/projection_5um']},
        'mouseID_522151-211806': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH1_projection/projection_5um']},
        'mouseID_522152-211807': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH1_projection/projection_5um']},
        'mouseID_586838-211801': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH1_projection/projection_5um']},
        'mouseID_586840-211802': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH1_projection/projection_5um']},
        'mouseID_588922-211800': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH1_projection/projection_5um']},
        'mouseID_588923-211799': {  # checked, works
            'contrast_limits': [0, 65535],
                                  'scale': (100, 0.35, 0.35),
                                  'url': [
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH1_projection/projection_0.350um',
                                      'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH1_projection/projection_5um']}

    # 'mouseID_': {
        #     'url': [
        #         '',
        #         ''
        #     ],
        #     'scale': (),
        #     'contrast_limits': [0, 65535]
        # },
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
        
        
        
    
    return datasets
    