import os

import PIL
from napari_plugin_engine import napari_hook_implementation

PIL.Image.MAX_IMAGE_PIXELS = 93312000000


def read_swc(path):
    from neurom import load_morphology
    import numpy as np
    from .fMOST_datasets import datasets

    m = load_morphology(path)
    print("Morphology loaded")
    data = []
    for n in m.neurites:
        for section in n.iter_sections():
            pts = section.points[:, :3]
            pts_x = pts[:, 0].copy()
            pts_y = pts[:, 1].copy()
            pts_z = pts[:, 2].copy()
            pts_rotated = np.empty_like(pts)
            pts_rotated[:, 0] = pts_z
            pts_rotated[:, 1] = pts_y
            pts_rotated[:, 2] = pts_x
            data.append(pts_rotated)
    meta = {
        "shape_type": 'path',
        "edge_width": 8,
        "edge_color": 'red',
        "name": "neuron tracings"
    }

    center_x, center_y, center_z = m.soma.center
    soma = [center_z, center_y, center_x]

    soma_meta = {
        "face_color": "yellow",
        "edge_color": "black",
        "size": 200,
        "name": "soma"
    }

    paths_tuple = (data, meta, 'shapes')
    soma_tuple = (soma, soma_meta, 'points')
    return [paths_tuple, soma_tuple]


@napari_hook_implementation
def napari_get_reader(path):
    if isinstance(path, str) and os.path.splitext(path)[1].lower() == '.swc':
        return read_swc
