import requests

from src.dexma.decorator import dexma_parser


class Locations(object):
    url_fragment = '/locations'

    def __init__(self, dexma):
        self.dexma = dexma
        self.url = self.dexma.base_url + self.url_fragment

    @dexma_parser
    def get_locations(self, params):
        response = requests.request(
            "GET",
            self.url,
            params=params,
            headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_location(self, location_id):
        url = f'{self.url}/{location_id}'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_location_devices(self, location_id):
        url = f'{self.url}/{location_id}/devices'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_location_referenced_devices(self, location_id):
        url = f'{self.url}/{location_id}/reference-devices'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_location_tags(self, location_id):
        url = f'{self.url}/{location_id}/tags'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response

    @dexma_parser
    def get_location_supplies(self, location_id):
        url = f'{self.url}/{location_id}/supplies'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers)
        return response

    # def get_valid_activities(self):
    #     response = requests.request(
    #         "GET",
    #         "https://api.dexma.com/v3/utility/global/activities",
    #         headers=HEADERS)
    #     return response
