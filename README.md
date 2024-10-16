# Data Space Service Client SDK

Basic client library for accessing the SmartOcean data space service to retrieve historical time series data from data sources.

## Data Space Service REST API

The SmartOcean dataspace service provides a REST API. The Swagger documentation is available via: https://dataspaceservice.jollywater-00619340.westus2.azurecontainerapps.io/docs

# Installation

The module is part of a collection of client modules for the SFI Smart Ocean platform under the sfisop namespace on ``pypi.org``.

## Installing as a module

To use the distributed module on pypi install this and other modules you may require for your Smart Ocean client
using pip:

```bash
pip install sfisop-dataspace-sdk
```

## Local installation
If you want to work on this module to test, debug, or develop, this module can be
installed locally on your system as source code. The path to the folder ``src`` needs to be in 
your PYTHONPATH. Then the module can be accessed from client code using:

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
pip install dist/sfisop_dataspace_sdk*.whl
```

## Sample Client Code

A sample implementation of the client-side code is provided in the `sample_client.py` file. 

It can be executed as:

```bash
python sample_client.py <path-to-configuration-file>
```

The code is to be used as a starting point for the implementation of the client applications.

A configuration file that can be used for the SmartOcean data space service can be found in the configs folder.

The data sources are currently available on the SmartOcean platform for demonstration purposes can be found in the `sample_datasources.py` file.

## Configuration and credentials        

The configuration file provided as on the command-line must contain the following information:

```
DATASPACE_BASE_URL: <base-url-for-dataspace-service>
DATASPACE_API_KEY_ID: DATASPACE_API_KEY
```

where the `DATASPACE_API_KEY` is the API key identifier that is contained in an `.env` file that must contain the following information:

```
DATASPACE_API_KEY = '<api-key>'
```

This indirect configuration of the API key makes it possible to share a single `.env` file for credentials across different deployments of the data space service.

The API key must be obtained from the SmartOcean data space service.
