# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:54:23 2023

@author: alpha
"""

datasets = {
    'mouseID_404421-182720':{
        'url':[
            'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH1',  # full res
            'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_404421-182720/CH2'
            ],
            'scale':(1,0.23,0.23)
        },
    
    'mouseID_405429-182725':{
        'url':[
            'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH1',  # full res
            'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/CH2'
            ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_418245-182727':{
        'url':[
            'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH1',
            'https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_418245-182727/CH2'
            ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_380471-191813':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380471-191813/CH2'  # full res
           ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_362188-191815':{
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362188-191815/CH2'
            ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_380470-191812':{
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_380470-191812/CH2'
            ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_426124-191808':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_426124-191808/CH2'
           ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_439168-191807':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_439168-191807/CH2'
           ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_443055-191805':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_443055-191805/CH2'
           ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_383680-18463':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383680-18463/CH2'
            ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_383128-18465':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/green/montage',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_383128-18465/red/montage'
            ],
        'scale':(1,0.23,0.23)
        },
    
    'mouseID_431038-191804':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_431038-191804/CH2'
            ],
        'scale':(1,0.35,0.35)
        },
    
    'mouseID_381488-18464':{
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381488-18464/CH2'
            ],
        'scale':(1,0.23,0.23)
        },
    
    'mouseID_423019-191803':{
        'url':[
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_423019-191803/CH2'
            ],
        'scale':(1,0.32,0.32)
        },

    'mouseID_373187-191817': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373187-191817/CH2'
        ],
        'scale': (1, 0.35, 0.35)
    },

    'mouseID_377387-18466': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_377387-18466/CH2'
        ],
        'scale': (1, 0.23, 0.23)
    },

    'mouseID_325875-17543': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/green/montage',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_325875-17543/red/montage'
        ],
        'scale': (1, 0.35, 0.35)
    },

    'mouseID_405426-182724': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_405426-182724/CH2'
        ],
        'scale': (1, 0.35, 0.35)
    },

    'mouseID_420489-191801': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_420489-191801/CH2'
        ],
        'scale': (1, 0.35, 0.35)
    },

    'mouseID_417571-182722': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417571-182722/CH2'
        ],
        'scale': (1, 0.23, 0.23)
    },

    'mouseID_417570-182721': {  # checked, works
        'url': [
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH1',  # full res
            'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_417570-182721/CH2'
        ],
        'scale': (1, 0.35, 0.35)
    },
    'mouseID_445241-211779': {  # checked, works
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH1'
                                ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445241-211779/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
    },
    'mouseID_445243-211780': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH1'
                                ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_445243-211780/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
    },
    'mouseID_467362-211782': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                     'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH1'
                                     ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_467362-211782/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
    },
    
    'mouseID_486478-196478': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                     'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH1'
                                    ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_486478-196478/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_494230-211775': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                     'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH1'
                                    ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_494230-211775/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_497458-211786': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                     'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH1'
                                    ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497458-211786/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_497462-211787': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497462-211787/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_497520-211776': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_497520-211776/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    'mouseID_500861-211788': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_500861-211788/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_510498-211777': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510498-211777/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_510502-211778': {
                              'scale': (1, 0.35, 0.35),
                               'url': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_510502-211778/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_522151-211806': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522151-211806/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_522152-211807': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_522152-211807/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_586838-211801': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586838-211801/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_586840-211802': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_586840-211802/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_588922-211800': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588922-211800/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },
    
    'mouseID_588923-211799': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH1'
                                  ],
                                'alt_ch': [
                                    'https://download.brainimagelibrary.org/ec/6a/ec6aac7d4d37b073/mouseID_588923-211799/CH2_10_10_10um'
                                    ],
                                'alt_scale': (10,10,10)
                              },

      # 'mouseID_210254-15257': {'scale_known': False,
      #                          'scale': (1, 0.35, 0.35),
      #                          'url': [
      #                               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_210254-15257/Green/Origin',   # full res
      #                               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_210254-15257/Red/Origin'  # full res
      #                          ]
      #                          },
      
     'mouseID_360835-18049': {
                              'scale': (1, 0.23, 0.23),
                              'url': [
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Green/montage',
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_360835-18049/Red/montage'
                              ]
                              },
     
     'mouseID_362191-191816': {
                               'scale': (1, 0.35, 0.35),
                               'url': [
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362191-191816/CH1',  # full res
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_362191-191816/CH2'
                               ]
                               },
     
     'mouseID_367667-18052': {
                              'scale': (1, 0.23, 0.23),
                              'url': [
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_367667-18052/Green/montage',
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_367667-18052/Red/montage'  # full res
                              ]
                              },
     
     # 'mouseID_373641-18462': {
     #                          'scale': (1, 0.35, 0.35),
     #                          'url': [
     #                               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373641-18462/CH1',  # full res
     #                               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_373641-18462/CH2'
     #                          ]
     #                          },
     
     'mouseID_374706-18461': {
                              'scale': (1, 0.35, 0.35),
                              'url': [
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374706-18461/CH1',  # full res
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374706-18461/CH2'
                              ]
                              },
     
     'mouseID_374707-18452': {
                              'scale': (1, 0.23, 0.23),
                              'url': [
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374707-18452/Green/montage',
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_374707-18452/Red/montage'  # full res
                              ]
                              },
     
      'mouseID_375394-18468': {'scale_known': False,
                               'scale': (1, 0.35, 0.35),
                               'url': [
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Green/montage',
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_375394-18468/Red/montage'
                               ]
                               },
      
      'mouseID_378667-18469': {'scale_known': False,
                               'scale': (1, 0.35, 0.35),
                               'url': [
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Green/montage',
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378667-18469/Red/montage'
                                   ]
                               },
      
      # 'mouseID_378668-18470': {'scale_known': False,
      #                          'scale': (1, 0.35, 0.35),
      #                          'url': [
      #                               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Green/montage',
      #                               'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_378668-18470/Red/montage'
      #                              ]
      #                          },
      
     'mouseID_381487-18458': {
                              'scale': (1, 0.23, 0.23),
                              'url': [
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381487-18458/green/montage',
                                   'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_381487-18458/red/montage'
                              ]
                              },
     
      'mouseID_394528-18867': {
                               'scale': (1, 0.23, 0.23),
                               'url': [
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_394528-18867/green'  # full res
                               ]
                               },
      
     'mouseID_411732-182718': {
                               'scale': (1, 0.35, 0.35),
                               'url': [
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_411732-182718/CH1',  # full res
                                    'https://download.brainimagelibrary.org/df/75/df75626840c76c15/mouseID_411732-182718/CH2'
                               ]
                               },
     
    '321237-17302': {'scale_known': False,
                    'scale': (1, 0.35, 0.35),
                      'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321237-17302/green',
                              'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321237-17302/red'
                              ]
                      },
    
      '321244-17545': {'scale_known': False,
                    'scale': (1, 0.35, 0.35),
                      'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321244-17545/green',
                              'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/321244-17545/red'
                              ]
                      },
      
      '326952-17304': {'scale_known': False,
                    'scale': (1, 0.35, 0.35),
                      'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/326952-17304/green',
                              'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/326952-17304/red'
                              ]
                      },
      
      # '339951-17781': {'scale_known': False,
      #               'scale': (1, 0.35, 0.35),
      #                 'url': ['https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/339951-17781/green',
      #                         'https://download.brainimagelibrary.org/94/77/94775d6a2ddab320/339951-17781/red'
      #                         ]
      #                 },
      
     '339952-17782': {
                      'scale': (1, 0.2, 0.2),
                      'url': [
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/339952-17782/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/339952-17782/red/montage'   # full_res
                      ]
                      },
     
     '351327-17787': {
                      'scale': (1, 0.23, 0.23),
                      'url': [
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351327-17787/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351327-17787/red/montage'   # full_res
                      ]
                      },
     
     '351331-17788': {
                      'scale': (1, 0.23, 0.23),
                      'url': [
                           'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351331-17788/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/351331-17788/red/montage'    # full_res
                      ]
                      },
     
     '355458-18053': {
                      'scale': (1, 0.23, 0.23),
                      'url': [
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355458-18053/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355458-18053/red/montage'   # full_res
                      ]
                      },
     
     '355459-18054': {
                      'scale': (1, 0.35, 0.35),
                      'url': [
                           'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/355459-18054/red/montage'
                      ]
                      },
     
     '358361-18047': {
                      'scale': (1, 0.23, 0.23),
                      'url': [
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/358361-18047/red/montage'
                      ]
                      },
     
     # '373367-18454': {
     #                  'scale': (1, 0.23, 0.23),
     #                  'url': [
     #                           'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373367-18454/green/montage',
     #                           'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373367-18454/red/montage'
     #                  ]
     #                  },
     
     # '373368-18455': {
     #                  'scale': (1, 0.23, 0.23),
     #                  'url': [
     #                           'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373368-18455/green/montage',
     #                           'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/373368-18455/red/montage'   # full_res
     #                  ]
     #                  },
     
     '381484-18457': {
                      'scale': (1, 0.23, 0.23),
                      'url': [
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/381484-18457/green/montage',
                               'https://download.brainimagelibrary.org/f1/dc/f1dcaeb016197373/381484-18457/red/montage'    # full_res
                      ]
                      },
     
     # '182683': {'scale_known': False,
     #                      'scale': (1, 0.35, 0.35),
     #                      'url': [
     #                           'https://download.brainimagelibrary.org/ec/d7/ecd76000aad716f8/182683/182683/CH1',
     #                           'https://download.brainimagelibrary.org/ec/d7/ecd76000aad716f8/182683/182683/CH2'
     #                      ]
     #                      },
     
     'mouseID_18011710-18066': {
                                'scale': (1, 0.23, 0.23),
                                'url': [
                                    'https://download.brainimagelibrary.org/df/8d/df8d3922f971e331/mouseID_18011710-18066/CH1'
                                    ]
                                },
     
     'mouseID_18011809-18072': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/73/ec/73ec63a56c799b6a/mouseID_18011809-18072/CH1'
                                    ]
                                },
     
     'mouseID_18011810-18073': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/2f/f9/2ff927b79ce7c247/mouseID_18011810-18073/CH1'
                                    ]
                                },
     
     'mouseID_18082503-18965': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/6d/b5/6db5ad6bbb46afcb/mouseID_18082503-18965/CH1'
                                ]
                                },
     
     'mouseID_18082506-18968': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/49/02/4902417b7c636fcc/mouseID_18082506-18968/CH1'
                                    ]
                                },
     
     'mouseID_18082513-18975': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/cf/6c/cf6cbb30bd18f3ad/mouseID_18082513-18975/CH1'
                                ]
                                },
     
     'mouseID_18082518-18980': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/05/79/057964871bc6ecfb/mouseID_18082518-18980/CH1'
                                ]
                                },
     
     'mouseID_18082519-18981': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/20/e9/20e90875c9ae4542/mouseID_18082519-18981/CH1'
                                ]
                                },
     
     'mouseID_18101517-182280': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/69/19/6919a5da8261ea78/mouseID_18101517-182280/CH1'
                                     ]
                                 },
     
     'mouseID_18103003-182051': {
                                 'scale': (2, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/e9/a2/e9a2af1aaa175f9b/mouseID_18103003-182051/CH1'
                                     ]
                                 },
     
     'mouseID_18103012-182056': {
                                 'scale': (2, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/21/7f/217f83338fcc1632/mouseID_18103012-182056/CH1'
                                     ]
                                 },
     
     'mouseID_18110102-182061': {
                                 'scale': (2, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/16/a5/16a50e365f275fc2/mouseID_18110102-182061/CH1'
                                     ]
                                 },
     
     'mouseID_18110103-182062': {
                                 'scale': (2, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/55/50/555003a95bda40ec/mouseID_18110103-182062/CH1'
                                     ]
                                 },
     
     'mouseID_18110108-182065': {
                                 'scale': (2, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/11/63/1163b556224cc1e6/mouseID_18110108-182065/CH1'
                                     ]
                                 },
     
     'mouseID_18110113-182069': {
                                 'scale': (2, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/07/51/0751d3f0a5bd672c/mouseID_18110113-182069/CH1'
                                     ]
                                 },
     
     'mouseID_18121215-182932': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/2e/31/2e31d0b226c4de3e/mouseID_18121215-182932/CH1'
                                     ]
                                 },
     
     'mouseID_19112221-195401': {
                                 'scale': (1, 0.325, 0.325),
                                 'url': [
                                      'https://download.brainimagelibrary.org/8a/f0/8af04b5469e576a7/mouseID_19112221-195401/CH1'
                                     ]
                                 },
     
      'mouseID_236174': {'scale_known': False,
                          'scale': (1, 0.35, 0.35),
                         'url': [
                             'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_236174/Raw-part1'
                             ]
                         },
      
      'mouseID_297974': {'scale_known': False,
                          'scale': (1, 0.35, 0.35),
                         'url': [
                             'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_297974/green',
                             'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_297974/red'
                             ]
                         },
      
      # 'mouseID_314107': {'scale_known': False,
      #                     'scale': (1, 0.35, 0.35),
      #                    'url': [
      #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_314107/green',
      #                        'https://download.brainimagelibrary.org/7f/53/7f537a62e521a26a/mouseID_314107/red'
      #                        ]
      #                    },
      
      # 'mouseID_327010-17298': {'scale_known': False,
      #                     'scale': (1, 0.35, 0.35),
      #                          'url': [
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_327010-17298/17298_1/Green/montage',
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_327010-17298/17298_1/Red/montage'
      #                              ]
      #                          },
      
      # 'mouseID_342870-17541': {'scale_known': False,
      #                     'scale': (1, 0.35, 0.35),
      #                          'url': [
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_342870-17541/green',
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_342870-17541/red'
      #                              ]
      #                          },
      
      # 'mouseID_344548-17542': {'scale_known': False,
      #                     'scale': (1, 0.35, 0.35),
      #                          'url': [
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_344548-17542/green',
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_344548-17542/red'
      #                              ]
      #                          },
      
      'mouseID_351325-17786': {'scale_known': False,
                          'scale': (1, 0.35, 0.35),
                               'url': [
                                   'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Green/montage',
                                   'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_351325-17786/Red/montage'
                                   ]
                               },
      
      # 'mouseID_369739-18459': {
      #                     'scale': (1, 0.23, 0.23),
      #                          'url': [
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_369739-18459/green',
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_369739-18459/red'
      #                              ]
      #                          },
      
      'mouseID_374712-18453': {
                          'scale': (1, 0.23, 0.23),
                               'url': [
                                   'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_374712-18453/green',
                                   'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_374712-18453/mouseID_374712-18453_CH2/red/montage'
                                   ]
                               },
      
      # 'mouseID_396477-18869': {
      #                          'scale': (1,0.35,0.35),
      #                          'url': [
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_396477-18869/green',
      #                              'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_396477-18869/red'
      #                              ]
      #                          },
      
     'mouseID_unknown-181349': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/6f/2c/6f2cea13d7d94efd/mouseID_unknown-181349/CH1'
                                    ]
                                },
     
    'mouseID_019081501-193388': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081501-193388/CH1'
                                      ]
                                  },
    
     'mouseID_019081503-193374': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081503-193374/CH1'
                                      ]
                                  },
     
     'mouseID_019081504-193375': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081504-193375/CH1'
                                      ]
                                  },
     
     'mouseID_019081505-193376': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081505-193376/CH1'
                                      ]
                                  },
     
     'mouseID_019081506-193377': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081506-193377/CH1'
                                      ]
                                  },
     
     'mouseID_019081507-193378': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081507-193378/CH1'
                                      ]
                                  },
     
     'mouseID_019081508-193379': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081508-193379/CH1'
                                      ]
                                  },
     
     'mouseID_019081510-193381': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081510-193381/CH1'
                                      ]
                                  },
     
     'mouseID_019081511-193382': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081511-193382/CH1'
                                      ]
                                  },
     
     'mouseID_019081512-193383': {
                                  'scale': (1, 0.23, 0.23),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081512-193383/CH1'
                                      ]
                                  },
     
     'mouseID_019081513-193385': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081513-193385/CH1'
                                      ]
                                  },
     
     'mouseID_019081514-193386': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081514-193386/CH1'
                                      ]
                                  },
     
     'mouseID_019081515-193387': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_019081515-193387/CH1'
                                      ]
                                  },
     
     'mouseID_18082502-18964': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/06/f4/06f4ef728fd23689/mouseID_18082502-18964/CH1'
                                    ]
                                },
     
     'mouseID_18082511-18973': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/95/39/953951d23ff7dee2/mouseID_18082511-18973/CH1'
                                    ]
                                },
     
     'mouseID_18082512-18974': {
                                'scale': (1, 0.35, 0.35),
                                'url': [
                                    'https://download.brainimagelibrary.org/94/27/9427ada8f2699b11/mouseID_18082512-18974/CH1'
                                    ]
                                },
     
     'mouseID_18101512-182275': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/36/cd/36cd086800a14408/mouseID_18101512-182275/CH1'
                                     ]
                                 },
     
     'mouseID_18101514-182278': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/52/2d/522d38ee2fea3ff5/mouseID_18101514-182278/CH1'
                                     ]
                                 },
     
     'mouseID_18112111-182448': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112111-182448/CH1'
                                     ]
                                 },
     
     'mouseID_18112613-182680': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112613-182680/CH1'
                                     ]
                                 },
     
     'mouseID_18112614-182681': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112614-182681/CH1'
                                     ]
                                 },
     
     'mouseID_18112615-182682': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18112615-182682/CH1'
                                     ]
                                 },
     
     'mouseID_18121216-182931': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_18121216-182931/CH1'
                                     ]
                                 },
     
     'mouseID_19010302-190132': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010302-190132/CH1'
                                     ]
                                 },
     
     'mouseID_19010303-190134': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010303-190134/CH1'
                                     ]
                                 },
     
     'mouseID_19010304-190133': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010304-190133/CH1'
                                     ]
                                 },
     
     'mouseID_19010305-190128': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010305-190128/CH1'
                                     ]
                                 },
     
     'mouseID_19010306-190130': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010306-190130/CH1'
                                     ]
                                 },
     
     'mouseID_19010307-190131': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010307-190131/CH1'
                                     ]
                                 },
     
     'mouseID_19010308-190129': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010308-190129/CH1'
                                     ]
                                 },
     
     'mouseID_19010309-190138': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010309-190138/CH1'
                                     ]
                                 },
     
     'mouseID_19010310-190135': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010310-190135/CH1'
                                     ]
                                 },
     
     'mouseID_19010312-190136': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19010312-190136/CH1'
                                     ]
                                 },
     
     'mouseID_19011801-190363': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011801-190363/CH1'
                                     ]
                                 },
     
     'mouseID_19011802-190364': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011802-190364/CH1'
                                     ]
                                 },
     
     'mouseID_19011803-190365': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011803-190365/CH1'
                                     ]
                                 },
     
     'mouseID_19011804-190366': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011804-190366/CH1'
                                     ]
                                 },
     
     'mouseID_19011805-190367': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011805-190367/CH1'
                                     ]
                                 },
     
     'mouseID_19011806-190368': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011806-190368/CH1'
                                     ]
                                 },
     
     'mouseID_19011807-190369': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011807-190369/CH1'
                                     ]
                                 },
     
     'mouseID_19011808-190370': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19011808-190370/CH1'
                                     ]
                                 },
     
     'mouseID_19012101-190381': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/a2/6b/a26b3e1028ce1f09/mouseID_19012101-190381/CH1'
                                     ]
                                 },
     
     'mouseID_19022512-190902': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022512-190902/CH1'
                                     ]
                                 },
     
     'mouseID_19022513-190891': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022513-190891/CH1'
                                     ]
                                 },
     
     'mouseID_19022514-190892': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022514-190892/CH1'
                                     ]
                                 },
     
     'mouseID_19022515-190900': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022515-190900/CH1'
                                     ]
                                 },
     
     'mouseID_19022516-190901': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022516-190901/CH1'
                                     ]
                                 },
     
     'mouseID_19022518_190903': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022518_190903/CH1'
                                     ]
                                 },
     
     'mouseID_19022519-190905': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022519-190905/CH1'
                                     ]
                                 },
     
     'mouseID_19022520-190904': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022520-190904/CH1'
                                     ]
                                 },
     
     'mouseID_19022521-190896': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022521-190896/CH1'
                                     ]
                                 },
     
     'mouseID_19022522-190895': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022522-190895/CH1'
                                     ]
                                 },
     
     'mouseID_19022523-190893': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022523-190893/CH1'
                                     ]
                                 },
     
     'mouseID_19022524-190894': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022524-190894/CH1'
                                     ]
                                 },
     
     'mouseID_19022525-190897': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022525-190897/CH1'
                                     ]
                                 },
     
     'mouseID_19022526-190898': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022526-190898/CH1'
                                     ]
                                 },
     
     'mouseID_19022714-190909': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022714-190909/CH1'
                                     ]
                                 },
     
     'mouseID_19022715-190906': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022715-190906/CH1'
                                     ]
                                 },
     
     'mouseID_19022716-190907': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022716-190907/CH1'
                                     ]
                                 },
     
     'mouseID_19022717-190908': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19022717-190908/CH1'
                                     ]
                                 },
     
     'mouseID_19030601-191223': {
                                 'scale': (1, 0.32, 0.32),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030601-191223/CH1'
                                     ]
                                 },
     
     'mouseID_19030602-191224': {
                                 'scale': (1, 0.32, 0.32),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030602-191224/CH1'
                                     ]
                                 },
     
     'mouseID_19030603-191225': {
                                 'scale': (2, 0.32, 0.32),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030603-191225/CH1'
                                     ]
                                 },
     
     'mouseID_19030606-191227': {
                                 'scale': (2, 0.32, 0.32),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030606-191227/CH1'
                                     ]
                                 },
     
     'mouseID_19030607-191192': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030607-191192/CH1'
                                     ]
                                 },
     
     'mouseID_19030608-191193': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030608-191193/CH1'
                                     ]
                                 },
     
     'mouseID_19030609-191194': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030609-191194/CH1'
                                     ]
                                 },
     
     'mouseID_19030610-191195': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030610-191195/CH1'
                                     ]
                                 },
     
     'mouseID_19030611-191196': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030611-191196/CH1'
                                     ]
                                 },
     
     'mouseID_19030612-191228': {
                                 'scale': (2, 0.32, 0.32),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030612-191228/CH1'
                                     ]
                                 },
     
     'mouseID_19030613-191229': {
                                 'scale': (2, 0.32, 0.32),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030613-191229/CH1'
                                     ]
                                 },
     
     'mouseID_19030614-191197': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030614-191197/CH1'
                                     ]
                                 },
     
     'mouseID_19030615-191198': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030615-191198/CH1'
                                     ]
                                 },
     
     'mouseID_19030616-191199': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19030616-191199/CH1'
                                     ]
                                 },
     
     'mouseID_19032503-191186': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032503-191186/CH1'
                                     ]
                                 },
     
     'mouseID_19032504-191187': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032504-191187/CH1'
                                     ]
                                 },
     
     'mouseID_19032505-191185': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032505-191185/CH1'
                                     ]
                                 },
     
     'mouseID_19032506-191184': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032506-191184/CH1'
                                     ]
                                 },
     
     'mouseID_19032507-191175': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032507-191175/CH1'
                                     ]
                                 },
     
     'mouseID_19032508-191171': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032508-191171/CH1'
                                     ]
                                 },
     
     'mouseID_19032509-191174': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032509-191174/CH1'
                                     ]
                                 },
     
     'mouseID_19032510-191173': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032510-191173/CH1'
                                     ]
                                 },
     
     'mouseID_19032511-191176': {
                                 'scale': (1, 0.23, 0.23),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032511-191176/CH1'
                                     ]
                                 },
     
     'mouseID_19032514-191183': {
                                 'scale': (100, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032514-191183/CH1'
                                     ]
                                 },
     
     'mouseID_19032515-191182': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032515-191182/CH1'
                                     ]
                                 },
     
     'mouseID_19032516-191180': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032516-191180/CH1'
                                     ]
                                 },
     
     'mouseID_19032517-191178': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032517-191178/CH1'
                                     ]
                                 },
     
     'mouseID_19032518-191177': {
                                 'scale': (100, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032518-191177/CH1'
                                     ]
                                 },
     
     'mouseID_19032519-191179': {
                                 'scale': (1, 0.35, 0.35),
                                 'url': [
                                      'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_19032519-191179/CH1'
                                     ]
                                 },
     
     'mouseID_463865-192341': {
                               'scale': (1, 0.35, 0.35),
                               'url': [
                                    'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_463865-192341/CH1'
                               ],
                           'alt_ch': [
                               'https://download.brainimagelibrary.org/ee/01/ee01a74d90e26226/mouseID_463865-192341/CH2_10_10_10um'
                               ],
                           'alt_scale': (10,10,10)
                               },
     
     'mouseID_w19051002-192869': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051002-192869/CH1'
                                      ]
                                  },
     
     'mouseID_w19051003-192868': {
                                  'scale': (1, 0.23, 0.23),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051003-192868/CH1'
                                      ]
                                  },
     
     'mouseID_w19051004-192867': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051004-192867/CH1'
                                      ]
                                  },
     
     'mouseID_w19051005-192870': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051005-192870/CH1'
                                      ]
                                  },
     
     'mouseID_w19051006-192865': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051006-192865/CH1'
                                      ]
                                  },
     
     'mouseID_w19051007-192858': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051007-192858/CH1'
                                      ]
                                  },
     
     'mouseID_w19051009-192860': {
                                  'scale': (1, 0.23, 0.23),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051009-192860/CH1'
                                      ]
                                  },
     
     'mouseID_w19051010-192861': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051010-192861/CH1'
                                      ]
                                  },
     
     'mouseID_w19051011-192855': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051011-192855/CH1'
                                      ]
                                  },
     
     'mouseID_w19051012-192856': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051012-192856/CH1'
                                      ]
                                  },
     
     'mouseID_w19051013-192862': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051013-192862/CH1'
                                      ]
                                  },
     
     'mouseID_w19051015-192853': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051015-192853/CH1'
                                      ]
                                  },
     
     'mouseID_w19051017-192863': {
                                  'scale': (1, 0.23, 0.23),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051017-192863/CH1'
                                      ]
                                  },
     
     'mouseID_w19051020-192857': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19051020-192857/CH1'
                                      ]
                                  },
     
     'mouseID_w19082902-193644': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082902-193644/CH1'
                                      ]
                                  },
     
     'mouseID_w19082904-193646': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082904-193646/CH1'
                                      ]
                                  },
     
     'mouseID_w19082905-193647': {
                                  'scale': (1, 0.23, 0.23),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082905-193647/CH1'
                                      ]
                                  },
     
     'mouseID_w19082908-193650': {
                                  'scale': (1, 0.23, 0.23),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082908-193650/CH1'
                                      ]
                                  },
     
     'mouseID_w19082909-193651': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082909-193651/CH1'
                                      ]
                                  },
     
     'mouseID_w19082922-193663': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082922-193663/CH1'
                                      ]
                                  },
     
     'mouseID_w19082925-193666': {
                                  'scale': (1, 0.35, 0.35),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19082925-193666/CH1'
                                      ]
                                  },
     
     'mouseID_w19091704-194089': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091704-194089/CH1'
                                      ]
                                  },
     
     'mouseID_w19091705-194090': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091705-194090/CH1'
                                      ]
                                  },
     
     'mouseID_w19091706-194091': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091706-194091/CH1'
                                      ]
                                  },
     
     'mouseID_w19091707-194092': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091707-194092/CH1'
                                      ]
                                  },
     
     'mouseID_w19091708-194093': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091708-194093/CH1'
                                      ]
                                  },
     
     'mouseID_w19091709-194094': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091709-194094/CH1'
                                      ]
                                  },
     
     'mouseID_w19091710-194095': {
                                  'scale': (1, 0.32, 0.32),
                                  'url': [
                                       'https://download.brainimagelibrary.org/00/9c/009c1e6fcc03ebac/mouseID_w19091710-194095/CH1'
                                      ]
                                  },
     
    
    }

# print("============================Total datasets:", len(datasets))


##################################################################################
##################################################################################

def test():
    import glob
    import os
    import tifffile
    import zarr
    
    errors = {}
    total_size = 0
    
    for num,idx in enumerate(datasets):
        print(f'##############   WORKING DATASET {num+1} of {len(datasets)}   ##################')
        current_dataset = datasets[idx]
        print(f'Testing dataset: {idx}')
        
        for u in current_dataset['url']:
            print(u)
            u = u.replace('https://download.brainimagelibrary.org/','/bil/data/')
            print(u)
            if os.path.exists(u):
                print(f'Path EXISTS: {u}')
                pass
            else:
                print(f'Path ABSENT: {u}')
                if idx not in errors:
                    errors[idx] = {}
                if 'url' not in errors[idx]:
                    errors[idx]['url'] = {}
                errors[idx]['url'][u] = False
        
        if idx in errors and 'url' in errors[idx]:
            print('A URL is not valid skipping all other steps')
            continue
        
            
        files = []
        first_file = []
        all_files = []
        for ii in current_dataset['url']:
            ii = ii.replace('https://download.brainimagelibrary.org/','/bil/data/')
            print(f'Globbing files: {ii}')
            lst = glob.glob(os.path.join(ii,'*.tif'))
            if len(lst) == 0:
                print(f'Globbing files: {ii}')
                lst = glob.glob(os.path.join(ii,'*.tiff'))
            
            print(f'Found {len(lst)} files')
            first_file.append(lst[0])
            files.append(len(lst))
            all_files = all_files + lst
            
        
        
        
        shapes = []
        for ii in first_file:
            try:
                print(f'Opening: {ii}')
                store = tifffile.imread(ii, aszarr=True)
                z = zarr.open(store, mode='r')
                shapes.append(z.shape)
                print(f'Shape: {z.shape}')
                del z
                del store
            except:
                print(f'Opening ERRORED: {ii}')
                errors[idx]['files']['num_match'] = 'No Open'
        
        
        if len(current_dataset['url']) > 1:
            ele = files[0]
            for ii in files:
                if ii != ele:
                    print('Num files not equal')
                    if idx not in errors:
                        errors[idx] = {}
                    if 'url' not in errors[idx]:
                        errors[idx]['url'] = {}
                    if 'num_match' not in errors[idx]['url']:
                        errors[idx]['url'] = {}
                    errors[idx]['url']['num_match'] = False
            
            ele = shapes[0]
            for ii in shapes:
                if ii != ele:
                    if idx not in errors:
                        errors[idx] = {}
                    if 'files' not in errors[idx]:
                        errors[idx]['files'] = {}
                    if 'shape_match' not in errors[idx]['files']:
                        errors[idx]['files']['shape_match'] = {}
                    errors[idx]['files']['shape_match'] = False
        
        for ff in all_files:
            total_size += os.path.getsize(ff)
            print(f'Collecting size: {ff} : {round(total_size/1024**4,2)} Terabytes : dset {num+1} of {len(datasets)}')
            

    return errors, total_size
    
