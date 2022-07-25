from src.dexma import reading
from unittest import TestCase


class ReadingTest(TestCase):

    def test_get_readings_by_parameter(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_key": 'EACTIVE'}
        response = rea.get_readings_by_parameter_key(params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["errors"][0]["message"],
                         "Resolution value cannot be empty")

    # Ver parameter_key con que resoluciones es compatible
    def test_get_readings_by_parameter_key_filter_by_date_err(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_key": 'EACTIVE',
                  "resolution": 'M',
                  "from": "2020-01-01T00:00:00",
                  "to":  "2021-01-01T00:00:00"}
        response = rea.get_readings_by_parameter_key(params)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()["errors"][0]["message"],
                         "Parameter 'EACTIVE' does not accept resolution 'MONTH' with specified operation")

    def test_get_readings_by_parameter_key_filter_without_dates(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_key": 'CURRENT',
                  "resolution": 'H'}
        response = rea.get_readings_by_parameter_key(params)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["errors"][0]["message"],
                         "May not be null")

    def test_get_readings_by_parameter_key_filter_by_date(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_key": 'CURRENT',
                  "resolution": 'H',
                  "from": "2020-01-01T00:00:00",
                  "to":  "2021-01-01T00:00:00"}
        response = rea.get_readings_by_parameter_key(params)
        self.assertEqual(response.status_code, 200)

    def test_get_readings_by_parameter_key_with_operation(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_key": 'CURRENT',
                  "resolution": 'H',
                  "from": "2020-01-01T00:00:00",
                  "to":  "2021-01-01T00:00:00",
                  "operation": 'MAX'}
        response = rea.get_readings_by_parameter_key(params)
        self.assertEqual(response.status_code, 200)

    def test_get_readings_by_parameter_id_voltage(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_id": 405,
                  "from": "2020-01-01T00:00:00",
                  "to":  "2021-01-01T00:00:00"}

        response = rea.get_readings_by_parameter_id(params)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"],
                         "Basic resolution does not support intervals greater than 1 month")

    # TO REVIEW - with an interval of two days, returns the same error
    def test_get_readings_by_parameter_id_power(self):
        rea = reading.Reading()
        params = {"device_id": 1043036,
                  "parameter_id": 401,
                  "from": "2020-01-01T00:00:00",
                  "to":  "2021-01-02T00:00:00"}

        response = rea.get_readings_by_parameter_id(params)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"],
                         "Basic resolution does not support intervals greater than 1 month")
