import requests
from dexma.decorator import dexma_parser


class Supplies(object):
    url_fragment = '/supplies'

    def __init__(self, dexma):
        self.dexma = dexma
        self.url = self.dexma.base_url + self.url_fragment

    @dexma_parser
    def get_energy_source_supplies(self, energy_source, params):
        url = f"{self.url}/{energy_source}"
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers,
            params=params)
        return response

    @dexma_parser
    def get_supply_devices(self, supply_id, energy_source):
        url = f"{self.url}/{energy_source}/{supply_id}"
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_supply(self, supply_id, energy_source):
        url = f"{self.url}/{energy_source}/{supply_id}"
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response
