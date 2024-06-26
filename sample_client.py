import requests

import client_config
import sample_datasources


class DataSpaceClient:

    def __init__(self, dataspace_config):
        self.base_url = dataspace_config.BASEURL
        self.api_key = dataspace_config.API_KEY

    def send_request(self,path):

        url = self.base_url + '/' + path

        headers = {
            'X-API-Key': self.api_key
        }

        response = requests.request("GET", url, headers=headers)

        return response

    def get_latest(self, datasource):

        response = self.send_request(f'v1/smartocean/{sample_datasources.HVLVIRTUAL}/sensors/latest')

        print(response.status_code)
        print(response.text)

        return response.text


if __name__ == '__main__':

    config_file = client_config.get_dataspace_configfile("DataSpace Configuration")
    dataspace_config = client_config.get_dataspace_config(config_file)

    client = DataSpaceClient(dataspace_config)

    client.get_latest("virtualsensorhub")



