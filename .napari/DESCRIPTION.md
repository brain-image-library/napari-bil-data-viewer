

# Description

This plugin enables viewing of datasets archived in the Brain Image Library.  

**NOTE: This plugin remains under early development.  Currently, only single color, fMOST datasets which include projections are available to view.  An example can be found here:  https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/



![Plugin Demo]( "Plugin Demo")

### Features

* Multiscale Rendering
  * Datasets which include multiple resolution representations of the data can be used for 
  https://download.brainimagelibrary.org/2b/da/2bdaf9e66a246844/mouseID_405429-182725/
* 3D rendering of whole datasets.  The lowest resolution will be used for rendering.
* The plugin does NOT require a BIL account as datasets are already accessible via https.

### Known Issues / limitations
* Currently the only datasets that are available are those which have been manually selected by the developers.  If you would like a specific dataset to be included please consider adding the dataset(s) to the dataset_info.py file and submitting a pull request:  https://github.com/brain-image-library/napari-bil-data-viewer/blob/main/napari_bil_data_viewer/dataset_info.py


----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-bil-data-viewer` via [pip]:

    pip install napari-bil-data-viewer

## Change Log:

##### <u>v0.1.0:</u>

Initial release.

## Contributing

Contributions by the community are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-bil-data-viewer" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/AlanMWatson/napari-imaris-loader/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
