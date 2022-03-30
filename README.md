Source : https://developers.dexma.com/

Type of data and dexma methods:

[SUPPLIES]
- get_energy_source_supplies: List all Supplies of the given Energy Source  
  Mandatory:
          Energy_source = ["GAS", "ELECTRICITY","WATER", "THERMAL", "EXPORTED_ELECTRICITY"]

  Filters:  
          name = Name of the supply. It will search supplies that start with.
          POD = CUPS id.
          start = Pagination start. Default 0
          limit = Pagination end. Default 20


- get_supplie_devices: List all Devices assigned to a Supply and their energy source.
  Mandatory:
            supply_id
            Energy_source = ["GAS", "ELECTRICITY","WATER", "THERMAL", "EXPORTED_ELECTRICITY"]


- get_supplie: Retrieve a Supply
  Mandatory:
            supply_id
            Energy_source = ["GAS", "ELECTRICITY","WATER", "THERMAL", "EXPORTED_ELECTRICITY"]


[DEVICES]
- get_devices: List all Devices
  Filters:  
          start
          limit
          datasource_id = Datapoint id.
          location_id
          localId = Device id used by de data insertion API to identify a device.
          param_key
          name
          status = ["ACCEPTED", "PENDING"]


- get_device: Retrieve a Device
  Mandatory:
            device_id


- get_datapoints: Retrieves a list of all Datapoints(datasources)
  Filters:
          start
          limit
          status = ["ACCEPTED", "PENDING", "REJECTED"]


[PARAMETERS]
- get_parameters: Retrieve list of parameters for the selected device and the selected filters.
  Mandatory:
          device_id

  Filters:  
          start
          limit
          name = Name of the parameter.


- get_resolutions: Retrieves a list of basic resolutions for the selected device.
  Mandatory:
            device_id

  Filters:
          from_
          to_


[READINGS]
- get_readings_by_parameter_key: Retrieve the Readings using a Parameter key for a specific time period for the selected device
  It's import check before the resolutions available for an specific parameter_key.
  (TO DO check all availables parameter_key and accepted resolutions)  
  Mandatory:
            device_id
            parameter_key
            resolution = ["FM", "TM", "QH", "HH", "H", "D", "W", "M", "B"]
            from_
            to_
  Filters:  
          operation = ["AVG", "MAX", "MIN", "DELTA", "RAW"]
          rounded


- get_readings_by_parameter_id: (Review their behaviour)
  Mandatory:
            device_id
            parameter_key          
            from_
            to_  


[LOCATIONS]
- get_locations: TO DO


- get_location
  Mandatory:
            location_id


- get_location_devices: Retrieve list of all Devices assigned to a Location.
  Mandatory:
            location_id


- get_location_referenced_devices: Retrieve list of Reference Devices of a Location.
  Mandatory:
            location_id


- get_location_tags: Retrieve list of Tags assigned to a Location.
  Mandatory:
            location_id


- get_location_supplies: Retrieve list of Supplies assigned to a Location.            
  Mandatory:
           location_id


- get_valid_activities: List all valid Activities for a Location.         
