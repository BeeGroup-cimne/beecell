from dexma import device
from dexma import location
from dexma import parameter
from dexma import reading
from dexma import supplie

from datetime import datetime

TYPE_STATUS = ["ACCEPTED", "PENDING"]
TYPE_STATUS_DATAPOINTS = ["ACCEPTED", "PENDING", "REJECTED"]
TYPE_OPERATIONS = ["AVG", "MAX", "MIN", "DELTA", "RAW"]
TYPE_RESOLUTION = ["FM", "TM", "QH", "HH", "H", "D", "W", "M", "B"]
TYPE_ENERGY_SOURCE = ["GAS", "ELECTRICITY", "WATER", "THERMAL", "EXPORTED_ELECTRICITY"]


class Device:
    def get_devices(
        self,
        start=0,
        limit=10,
        datasource_id=None,
        location_id=None,
        localId=None,
        param_key=None,
        name=None,
        status=None,
    ):
        params = {}
        if start:
            params["start"] = start
        if limit:
            params["limit"] = limit
        if datasource_id:
            params["datasource_id"] = datasource_id
        if location_id:
            params["location_id"] = location_id
        if localId:
            params["localId"] = localId
        if param_key:
            params["param_key"] = param_key
        if name:
            params["name"] = name
        if status and status in TYPE_STATUS:
            params["status"] = status

        dev = device.Device()
        response = dev.get_devices(params)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_device(self, device_id):
        dev = device.Device()
        response = dev.get_device(device_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_datapoints(self, device_id, start=0, limit=20, status=[]):
        params = {}
        if start:
            params["start"] = start
        if limit:
            params["limit"] = limit
        if status and set(status).intersection(TYPE_STATUS_DATAPOINTS) == set(status):
            params["status"] = status
        dev = device.Device()
        response = dev.get_datapoints(device_id, params)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_datasource(datasource_id):
        dev = device.Device()
        response = dev.get_datasource(datasource_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")


class Parameter:
    def get_parameters(self, device_id, start=0, limit=20, name=None):
        params = {}
        if start:
            params["start"] = start
        if limit:
            params["limit"] = limit
        if name:
            params["name"] = name
        par = parameter.Parameter()
        response = par.get_parameters(device_id, params)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_resolutions(self, device_id, from_, to_):
        params = {
            "from": datetime.strptime(from_, "%Y-%m-%d").isoformat(),
            "to": datetime.strptime(to_, "%Y-%m-%d").isoformat(),
        }
        par = parameter.Parameter()
        response = par.get_resolutions(device_id, params)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")


class Reading:
    def get_readings_by_parameter_key(
        self,
        device_id,
        parameter_key,
        resolution,
        from_,
        to_,
        operation=None,
        rounded=None,
    ):
        if resolution in TYPE_RESOLUTION:
            if parameter_key and resolution and from_ and to_:
                params = {}
                params["device_id"] = device_id
                params["resolution"] = resolution
                params["parameter_key"] = parameter_key
                params["from"] = datetime.strptime(from_, "%Y-%m-%d").isoformat()
                params["to"] = datetime.strptime(to_, "%Y-%m-%d").isoformat()
                if operation and operation in TYPE_OPERATIONS:
                    params["operation"] = operation
                if rounded:
                    if (
                        len(rounded.split("_")) > 1
                        and rounded.split("_")[0] == "DECIMALS"
                        and type(rounded.split("_")[1]) == int
                    ):
                        params["rounded"] = rounded
                rea = reading.Reading()
                response = rea.get_readings_by_parameter_key(params)
                if response.status_code == 200:
                    print(response.json())
                else:
                    print(f"{response.status_code}:{response.text}")

    def get_readings_by_parameter_id(
        self,
        device_id,
        parameter_id,
        from_,
        to_,
        rounded=None,
    ):
        if parameter_id and from_ and to_:
            params = {}
            params["device_id"] = device_id
            params["parameter_id"] = parameter_id
            params["from"] = datetime.strptime(from_, "%Y-%m-%d").isoformat()
            params["to"] = datetime.strptime(to_, "%Y-%m-%d").isoformat()
            if rounded:
                if (
                    len(rounded.split("_")) > 1
                    and rounded.split("_")[0] == "DECIMALS"
                    and type(rounded.split("_")[1]) == int
                ):
                    params["rounded"] = rounded
            rea = reading.Reading()
            response = rea.get_readings_by_parameter_id(params)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"{response.status_code}:{response.text}")


class Supplie:
    def get_energy_source_supplies(
        self, energy_source, name=None, POD=None, start=0, limit=20
    ):
        if energy_source in TYPE_ENERGY_SOURCE:
            params = {}
            if name:
                params["name"] = name
            if POD:
                params["POD"] = POD
            if start:
                params["start"] = start
            if limit:
                params["limit"] = limit
            sup = supplie.Supplie()
            response = sup.get_energy_source_supplies(energy_source, params)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"{response.status_code}:{response.text}")

    def get_supplie_devices(self, supply_id, energy_source):
        if energy_source in TYPE_ENERGY_SOURCE:
            sup = supplie.Supplie()
            response = sup.get_supplie_devices(supply_id, energy_source)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"{response.status_code}:{response.text}")

    def get_supplie(self, supply_id, energy_source):
        if energy_source in TYPE_ENERGY_SOURCE:
            sup = supplie.Supplie()
            response = sup.get_supplie(supply_id, energy_source)
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"{response.status_code}:{response.text}")


class Location:
    def get_locations(
        self,
        name=None,
        key=None,
        tags=None,
        device_id=None,
        area_units=None,
        temps_units=None,
    ):
        params = {}
        if name:
            params["name"] = name
        if key:
            params["key"] = key
        if device_id:
            params["device_id"] = device_id
        if area_units:
            params["area_units"] = area_units
        if temps_units:
            params["temps_units"]
        loc = location.Location()
        response = loc.get_locations(params)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_location(self, location_id):
        loc = location.Location()
        response = loc.get_location(location_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_location_devices(self, location_id):
        loc = location.Location()
        response = loc.get_location_devices(location_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_location_referenced_devices(self, location_id):
        loc = location.Location()
        response = loc.get_location_referenced_devices(location_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_location_tags(self, location_id):
        loc = location.Location()
        response = loc.get_location_tags(location_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_location_supplies(self, location_id):
        loc = location.Location()
        response = loc.get_location_supplies(location_id)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")

    def get_valid_activities(self):
        loc = location.Location()
        response = loc.get_valid_activities()
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"{response.status_code}:{response.text}")


if __name__ == "__main__":
    loc = Location()
    loc.get_locations()

    dev = Device()
    dev.get_devices()
