# DataSpace Service Client SDK

The Swagger documentation for the data space service is available via: https://dataspaceservice.jollywater-00619340.westus2.azurecontainerapps.io/docs

# Installing as a module

The module is part of a collection of client modules for the SFI Smart Ocean platform under the sfisop namespace on ``pypi.org``.

To use the distributed module on pypi install this and other modules you may require for your Smart Ocean client
using pip:

```bash
pip install sfisop-dataspace-sdk
```

## Local installation with pip

If you want to work on this module to test, debug, or develop, this module can be
installed locally on your system as source code. The path to the folder ``src`` needs to be in 
your `PYTHONPATH`. Then the module can be accessed from client code using:

```python
import sfisop.dataspace_sdk
```

In addition, install the dependencies needed for this module in your ``python`` environment using the
``requirements.txt`` in the root folder:


```bash 
python3 -m pip install -r requirements.txt
```

Setup `PYTHONPATH` to include the ``src`` folder:

```
export PYTHONPATH=<path to top-level folder>/dataspace_sdk/src/
```

# Installation with poetry

You can install this module on your system locally using ``poetry`` (https://python-poetry.org/). You might want to do
this if you have made some local changes to the code and want to install them in your environment.
To do this install ``poetry`` and execute the following commands:

```bash
poetry build
pip install dist/ sfisop_dataspace_sdk-<version>-py3-none-any.whl
```
