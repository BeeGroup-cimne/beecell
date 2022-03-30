import dexma
from unittest import TestCase

# TYPE_ENERGY_SOURCE = ["GAS", "ELECTRICITY",
#                      "WATER", "THERMAL", "EXPORTED_ELECTRICITY"]


class SupplieTest(TestCase):

    def test_get_energy_source_supplies_without_params(self):
        params = {}
        sup = dexma.Supplie()
        response = sup.get_energy_source_supplies("ELECTRICITY", params)
        self.assertEqual(response.status_code, 200)

    def test_get_supplie_device(self):
        sup = dexma.Supplie()
        response = sup.get_supplie_devices(21556, "ELECTRICITY")
        self.assertEqual(response.status_code, 200)

    def test_get_supplie_device_no_data(self):
        sup = dexma.Supplie()
        response = sup.get_supplie_devices(21556, "WATER")
        self.assertEqual(response.status_code, 204)  # No content

    def test_get_supplie(self):
        sup = dexma.Supplie()
        response = sup.get_supplie(21556, "ELECTRICITY")
        self.assertEqual(response.status_code, 200)
