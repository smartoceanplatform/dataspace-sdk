# Data Space Service Client SDK

Basic client library for accessing the SmartOcean data space service to retreive historical time series data from data sources.

## Data Space Service REST API

The SmartOcean dataspace service provides a REST API. The Swagger documentation is available via: https://dataspaceservice.jollywater-00619340.westus2.azurecontainerapps.io/docs

## Installation

First step is to install the required dependencies into your Python environment.
```bash 
python3 -m pip install -r requirements.txt
```

## Sample Client Code

A sample implementation of the client-side code is provided in the `sample_client.py` file. 

It can be executed as:

```bash
python sample_client.py <path-to-configuration-file>
```

The code is to be used as a starting point for the implementation of the client applications.

A configuration file that can be used for the SmartOcean data space service can be found in the configs folder.

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
