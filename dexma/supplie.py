import os

import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "x-dexcell-token": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}


class Supplie(object):
    base_url = "https://api.dexma.com/v3/utility/supplies"

    @classmethod
    def get_energy_source_supplies(cls, energy_source, params):
        url = f"{cls.base_url}/{energy_source}"
        response = requests.request(
            "GET",
            url,
            headers=HEADERS,
            params=params)
        return response

    @classmethod
    def get_supplie_devices(cls, supplie_id, energy_source):
        url = f"{cls.base_url}/{energy_source}/{supplie_id}"
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    @classmethod
    def get_supplie(cls, supplie_id, energy_source):
        url = f"{cls.base_url}/{energy_source}/{supplie_id}"
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response
