import requests

from src.dexma.decorator import dexma_parser


class Readings(object):
    url_fragment = '/readings'

    def __init__(self, dexma):
        self.dexma = dexma
        self.url = self.dexma.base_url + self.url_fragment

    @dexma_parser
    def get_readings_by_parameter_key(self, params):
        response = requests.request(
            "GET",
            self.url,
            headers=self.dexma.headers,
            params=params)
        return response

    @dexma_parser
    def get_readings_by_parameter_id(self, params):
        response = requests.request(
            "GET",
            self.url + "/by-parameter-id",
            headers=self.dexma.headers,
            params=params)
        return response
