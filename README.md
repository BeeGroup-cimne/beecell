Source : https://developers.dexma.com/

## Type of data and dexma methods:
### [SUPPLIES]
##### get_energy_source_supplies: List all Supplies of the given Energy Source  
 Mandatory parameters:
 * Energy_source

 |Energy_source|
 | ------ |
 |GAS|
 |ELECTRICITY|
 |WATER|
 |THERMAL|
 |EXPORTED_ELECTRICITY|

  Filters:  
  - name = Name of the supply. It will search supplies that start with.
  - POD = CUPS id.
  - start = Pagination start. Default 0
  - limit = Pagination end. Default 20

##### get_supplie_devices: List all Devices assigned to a Supply and their energy source.
 Mandatory parameters:  
 * Supply_id
 * Energy_source

 |Energy_source|
 | ------ |
 |GAS|
 |ELECTRICITY|
 |WATER|
 |THERMAL|
 |EXPORTED_ELECTRICITY|

 ##### get_supplie: Retrieve a Supply
 Mandatory parameters:
 * Supply_id
 * Energy_source

 |Energy_source|
 | ------ |
 |GAS|
 |ELECTRICITY|
 |WATER|
 |THERMAL|
 |EXPORTED_ELECTRICITY|



### [DEVICES]
##### get_devices: List all Devices
  Filters:  
  - start
  - limit
  - datasource_id = Datapoint id.
  - location_id
  - localId = Device id used by de data insertion API to identify a device.
  - param_key
  - name
  - status = ["ACCEPTED", "PENDING"]


##### get_device: Retrieve a Device
  Mandatory parameter:
  * device_id


##### get_datapoints: Retrieves a list of all Datapoints(datasources)
  Filters:
  - start
  - limit
  - status = ["ACCEPTED", "PENDING", "REJECTED"]


### [PARAMETERS]
Dexma Parameters doc: https://docs.google.com/spreadsheets/d/1W97Yv9UWR9iwmXzknxSQSiIzjt4capmWuaZsAwNJD0g/pub?hl=en&hl=en&single=true&gid=0&output=html

##### get_parameters: Retrieve list of parameters for the selected device and the selected filters.
  Mandatory paramaters:
  * device_id

  Filters:  
  - start
  - limit
  - name = Name of the parameter.


##### get_resolutions: Retrieves a list of basic resolutions for the selected device.
  Mandatory parameters:
  * device_id

  Filters:
  - from_
  - to_


### [READINGS]
##### get_readings_by_parameter_key: Retrieve the Readings using a Parameter key for a specific time period for the selected device
  It's import check before the resolutions available for an specific parameter_key.
  (TO DO check all availables parameter_key and accepted resolutions)  
  Mandatory parameters:
  * device_id
  * parameter_key
  * resolution = ["FM", "TM", "QH", "HH", "H", "D", "W", "M", "B"]
  * from_
  * to_

  |Resolution type|Description|
  | ------ | ------- |
  |FM      |Unknown|
  |TM      |Unknown|
  |QH      |Quarter hourly|
  |HH      |Unknown|
  |H       |Hourly|
  |D       |Daily|
  |W       |Weekly|
  |M       |Monthly|
  |B       |Unknown|

  Filters:  
  - operation = ["AVG", "MAX", "MIN", "DELTA", "RAW"]
  - rounded


##### get_readings_by_parameter_id: (Review their behaviour)
  Mandatory parameters:
  * device_id
  * parameter_key          
  * from_
  * to_  


### [LOCATIONS]
##### get_locations: Retrieve a list of all Locations.
Filters:
- name
- key
- tags
- device_id
- area_units
- temp_units


##### get_location: Retrieve a Location.
  Mandatory parameters:
  * location_id


##### get_location_devices: Retrieve list of all Devices assigned to a Location.
  Mandatory parameters:
  * location_id


##### get_location_referenced_devices: Retrieve list of Reference Devices of a Location.
  Mandatory parameters:
  * location_id


##### get_location_tags: Retrieve list of Tags assigned to a Location.
  Mandatory parameters:
  * location_id


##### get_location_supplies: Retrieve list of Supplies assigned to a Location.            
  Mandatory parameters:
  * location_id


##### get_valid_activities: List all valid Activities for a Location.
  Mandatory parameters:
  * location_id
