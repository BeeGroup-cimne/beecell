import os

import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "x-dexcell-token": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}


class Parameter(object):
    base_url = "https://api.dexma.com/v3/parameters"

    @classmethod
    def get_parameters(cls, device_id, params):
        params["device_id"] = device_id
        response = requests.request(
            "GET", cls.base_url, headers=HEADERS, params=params)
        return response

    @classmethod
    def get_resolutions(cls, device_id, params):
        params["device_id"] = device_id
        response = requests.request(
            "GET",
            "https://api.dexma.com/v3/parameters/CDD/resolution",
            headers=HEADERS,
            params=params)
        return response
