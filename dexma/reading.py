import os

import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "x-dexcell-token": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}


class Reading(object):
    base_url = "https://api.dexma.com/v3/readings"

    @classmethod
    def get_readings_by_parameter_key(cls, params):
        response = requests.request(
            "GET",
            cls.base_url,
            headers=HEADERS,
            params=params)
        return response

    @classmethod
    def get_readings_by_parameter_id(cls, params):
        response = requests.request(
            "GET",
            cls.base_url + "/by-parameter-id",
            headers=HEADERS,
            params=params)
        return response
