import requests
import datetime
import urllib

import client_config
import sample_datasources


class DataSpaceClient:

    def __init__(self, dataspace_config):
        self.base_url = dataspace_config.BASEURL
        self.api_key = dataspace_config.API_KEY

    def send_request(self,path):

        url = self.base_url + '/' + path

        headers = {
            'X-API-Key': self.api_key,
            'accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        return response

    def get_latest(self, datasource):

        response = self.send_request(f'v1/smartocean/{datasource}/sensors/latest')

        return response

    def get_period(self, datasource, start: datetime.datetime, end: datetime.datetime):

        # TODO: validate that start is earlier than end
        start_time = urllib.parse.quote(start.isoformat())
        end_time = urllib.parse.quote(end.isoformat())

        response = self.send_request(f'v1/smartocean/{datasource}/sensors/?start={start_time}&end={end_time}')

        return response


if __name__ == '__main__':

    config_file = client_config.get_dataspace_configfile("DataSpace Configuration")
    dataspace_config = client_config.get_dataspace_config(config_file)

    client = DataSpaceClient(dataspace_config)

    response_latest = client.get_latest(sample_datasources.HVLVIRTUAL)
    print(response_latest.status_code)
    print(response_latest.text)

    start_time = datetime.datetime(2024, 6, 1, 0, 0, 0)
    end_time = datetime.datetime(2024, 6, 7, 0, 0, 0)

    response_period = client.get_period(sample_datasources.HVLVIRTUAL, start_time, end_time)
    print(response_period.status_code)
    print(response_period.text)