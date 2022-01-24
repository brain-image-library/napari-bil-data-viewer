
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"


from .bil_data_loader_widget import napari_experimental_provide_dock_widget
#from .dataset_info import get_datasets



