# DataSpace Service Client SDK

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
