import requests

HEADERS = {
    "x-dexcell-token": "fca21ca1e332e8d13e74",
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
