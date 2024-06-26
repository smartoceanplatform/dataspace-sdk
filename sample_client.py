import requests

import client_config


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

    def virtualnode_get_latest(self):

        response = self.send_request('v1/smartocean/virtualsensorhub/sensors/latest')

        print(response.status_code)
        print(response.text)


if __name__ == '__main__':

    config_file = client_config.get_dataspace_configfile("DataSpace Configuration")
    dataspace_config = client_config.get_dataspace_config(config_file)

    client = DataSpaceClient(dataspace_config)

    client.virtualnode_get_latest()



