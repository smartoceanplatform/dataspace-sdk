from sfisop.dataspace_sdk.sample_client import DataSpaceClient
from sfisop.dataspace_sdk.client_config import get_dataspace_config
from sfisop.dataspace_sdk import sample_datasources 
import requests
import datetime



def test_dataspace_config():
    config_file = 'configs/config-dataspace-prod.yml'
    dataspace_config = get_dataspace_config(config_file)
    client = DataSpaceClient(dataspace_config)

    response_latest = client.get_latest(sample_datasources.HVLVIRTUAL)
    print(response_latest.status_code)
    print(response_latest.text)

    start_time = datetime.datetime(2024, 6, 1, 0, 0, 0)
    end_time = datetime.datetime(2024, 6, 7, 0, 0, 0)

    response_period = client.get_period(sample_datasources.HVLVIRTUAL, start_time, end_time)
    print(response_period.status_code)
    print(response_period.text)

    assert response_latest is not None & response_period is not None
