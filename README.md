

# Description

This plugin enables viewing of select Brain Image Library datasets



# Install

```python
conda create -y -n bil-viewer python=3.8
conda activate bil-viewer

pip install -e /path/to/cloned/repo/

# Run napari
napari
```

# Use

Plugins > napari-bil-data-viewer: load_bil_data

Select dataset from the panel

Click 'Load Dataset'



Most datasets are multi-resolution.  The lowest resolution will load quickly, but when zooming in, napari may pause briefly while the next resolution is loaded.
