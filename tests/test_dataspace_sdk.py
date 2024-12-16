from sfisop.dataspace_sdk.client import DataSpaceClient
from sfisop.dataspace_sdk.config import get_dataspace_config
from sfisop.dataspace_sdk import sop_datasources

import datetime
import json

import unittest


class DataSpaceSDKTest(unittest.TestCase):

    def setUp(self):
        config_file = 'configs/config-dataspace-prod.yml'
        self.dataspace_config = get_dataspace_config(config_file)
        self.data_sources = ['virtualsensorhub', 'austevollsouth', 'austevollsouth', 'wsenseaustevoll1', 'wsenseaustevoll2']

    def test_get_latest(self):
        client = DataSpaceClient(self.dataspace_config)

        for datasource in self.data_sources:

            response = client.get_latest(datasource)

            self.assertIsNotNone(response)

            if response.status_code != 200:
                print(f'{datasource}[{response.status_code}]')
            else:
                ts_data_dict = json.loads(response.text)

                ts = ts_data_dict['data']['time']
                print(f'{datasource} [{ts}]')

    def test_get_period(self):
        client = DataSpaceClient(self.dataspace_config)

        start_time = datetime.datetime(2024, 6, 1, 0, 0, 0)
        end_time = datetime.datetime(2024, 6, 7, 0, 0, 0)

        response = client.get_period(sop_datasources.HVLVIRTUAL, start_time, end_time)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()