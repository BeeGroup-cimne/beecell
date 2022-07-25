import os

import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "x-dexcell-token": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}


class Device(object):
    base_url = "https://api.dexma.com/v3/devices"

    @classmethod
    def get_devices(cls, params):
        response = requests.request(
            "GET", cls.base_url, headers=HEADERS, params=params)
        return response

    @classmethod
    def get_device(cls, device_id):
        response = requests.request(
            "GET", f"{cls.base_url}/{device_id}", headers=HEADERS)
        return response

    @classmethod
    def get_datapoints(cls, device_id, params):
        response = requests.request(
            "GET", f"{cls.base_url}/{device_id}/datapoints",
            headers=HEADERS,
            params=params
        )
        return response

    @classmethod
    def get_datasource(cls, datasource_id):
        response = requests.request(
            "GET", f"{cls.base_url}/datasources/{datasource_id}",
            headers=HEADERS
        )
        return response
