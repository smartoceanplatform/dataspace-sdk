# Data Space Service Client SDK

Client library of accessing the SmartOcean data space service in order to retreive time series data from the data sources.

## Installation

```bash 
python -m pip install -r requirements.txt
```

## Sample Client Code

A sample implementation of the client code is provided in the `sample_client.py` file. The client code is to be used as a reference for the implementation of the client code in the user application.

## Configuration and credentials        

The configuration file provided as command line must contain the following information:

```
DATASPACE_BASE_URL: <base-url-for-dataspace-service>
DATASPACE_API_KEY_ID: DATASPACE_PROD_API_KEY
```

where the DATASPACE_PROD_API_KEY is the API key identifier that is contained in an .env file that must contain the following information:

```
DATASPACE_PROD_API_KEY = '<api-key>'
```

This indirect configuration of the API key makes it possible to share a single .env file for credentials between different deployments of the data space service.

This API key is to be obtained from the SmartOcean data space service.