import requests

from dexma.decorator import dexma_parser


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

    @dexma_parser
    def get_resolutions(self, device_id, p_key, params):
        params["device_id"] = device_id
        response = requests.request(
            "GET",
            f"https://api.dexma.com/v3/parameters/{p_key}/resolutions",
            headers=self.dexma.headers,
            params=params)
        return response
