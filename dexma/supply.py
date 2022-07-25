import os

import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "x-dexcell-token": os.getenv("DEXMA_API_KEY"),
    "Content-Type": "application/json",
}


class Supply(object):
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
    def get_supply_devices(cls, supplie_id, energy_source):
        url = f"{cls.base_url}/{energy_source}/{supplie_id}"
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response

    @classmethod
    def get_supply(cls, supplie_id, energy_source):
        url = f"{cls.base_url}/{energy_source}/{supplie_id}"
        response = requests.request(
            "GET",
            url,
            headers=HEADERS)
        return response
