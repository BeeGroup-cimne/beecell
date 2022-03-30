import dexma
from unittest import TestCase
# import sys
# sys.path.append('./')


class DevicesTest(TestCase):

    def test_get_devices_no_parameter(self):
        dev = dexma.Device()
        params = {}
        response = dev.get_devices(params)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(response.json()), list)

    def test_get_devices_with_valid_parameters(self):
        dev = dexma.Device()
        params = {"start": 0, "limit": 20, "status": ["ACCEPTED"]}
        response = dev.get_devices(params)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(response.json()), list)

    def test_get_devices_with_invalid_status(self):
        dev = dexma.Device()
        params = {"start": 0, "limit": 20, "status": "INCOMPLETE"}
        response = dev.get_devices(params)
        self.assertEqual(response.status_code, 400)
