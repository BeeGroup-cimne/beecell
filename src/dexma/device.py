import requests

from src.dexma.decorator import dexma_parser


class Device(object):
    url_fragment = '/devices'

    def __init__(self, dexma):
        self.dexma = dexma
        self.url = self.dexma.base_url + self.url_fragment

    @dexma_parser
    def get_devices(self, params):
        response = requests.request(
            "GET", self.url, headers=self.dexma.headers, params=params)
        return response

    @dexma_parser
    def get_device(self, device_id):
        response = requests.request(
            "GET", f"{self.url}/{device_id}", headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_datapoints(self, device_id, params):
        response = requests.request(
            "GET", f"{self.url}/{device_id}/datapoints",
            headers=self.dexma.headers,
            params=params
        )
        return response

    @dexma_parser
    def get_datasource(self, datasource_id):
        response = requests.request(
            "GET", f"{self.url}/datasources/{datasource_id}",
            headers=self.dexma.headers
        )
        return response
