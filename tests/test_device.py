from dexma import device
from unittest import TestCase


class DeviceTest(TestCase):

    def test_get_device_without_id(self):
        dev = device.Device()
        try:
            dev.get_device()
        except Exception as e:
            e == self.assertRaises(TypeError)

    def test_get_device_invalid_id(self):
        dev = device.Device()
        response = dev.get_device('asde333')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Bad Request")

    def test_get_device_no_exist_id(self):
        dev = device.Device()
        response = dev.get_device(2222222)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()["message"], "Entity not found")

    def test_get_device_valid_id(self):
        dev = device.Device()
        response = dev.get_device(1043036)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), dict)

    def test_get_device_datapoints(self):
        dev = device.Device()
        params = {"start": 0, "limit": 10, "status": ["PENDING", "REJECTED"]}
        response = dev.get_datapoints(1043036, params)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(response.json()), list)

    def test_get_device_datapoints_without_params(self):
        dev = device.Device()
        response = dev.get_datapoints(1043036, {})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(response.json()), list)
