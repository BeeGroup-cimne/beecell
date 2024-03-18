import requests

from src.dexma.decorator import dexma_parser


class Parameters(object):
    url_fragment = '/parameters'

    def __init__(self, dexma):
        self.dexma = dexma
        self.url = self.dexma.base_url + self.url_fragment

    @dexma_parser
    def get_parameters(self, device_id, params):
        params["device_id"] = device_id
        response = requests.request(
            "GET", self.url, headers=self.dexma.headers, params=params)
        return response

    # def get_resolutions(cls, device_id, params):
    #     params["device_id"] = device_id
    #     response = requests.request(
    #         "GET",
    #         "https://api.dexma.com/v3/parameters/CDD/resolution",
    #         headers=self.dexma.headers,
    #         params=params)
    #     return response
