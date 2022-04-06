import requests

HEADERS = {
    "x-dexcell-token": "fca21ca1e332e8d13e74",
    "Content-Type": "application/json",
}


class Location(object):
    base_url = "https://api.dexma.com/v3/utility/locations"

    @classmethod
    def get_locations(cls, params):
        response = requests.request(
            "GET",
            cls.base_url,
            params=params,
            headers=HEADERS)
        return response

    @classmethod
    def get_location(cls, location_id):
        url = f'{cls.base_url}/{location_id}'
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    def get_location_devices(cls, location_id):
        url = f'{cls.base_url}/{location_id}/devices'
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    def get_location_referenced_devices(cls, location_id):
        url = f'{cls.base_url}/{location_id}/reference-devices'
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    def get_location_tags(cls, location_id):
        url = f'{cls.base_url}/{location_id}/tags'
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    def get_location_supplies(cls, location_id):
        url = f'{cls.base_url}/{location_id}/supplies'
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    def get_valid_activities(cls):
        response = requests.request(
            "GET",
            "https://api.dexma.com/v3/utility/global/activities",
            headers=HEADERS)
        return response
