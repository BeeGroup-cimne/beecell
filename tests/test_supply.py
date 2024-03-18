# from unittest import TestCase
#
# from src.dexma import supply
#
#
# # TYPE_ENERGY_SOURCE = ["GAS", "ELECTRICITY",
# #                      "WATER", "THERMAL", "EXPORTED_ELECTRICITY"]
#
#
# class SupplyTest(TestCase):
#
#     def test_get_energy_source_supplies_without_params(self):
#         params = {}
#         sup = supply.Supply()
#         response = sup.get_energy_source_supplies("ELECTRICITY", params)
#         self.assertEqual(response.status_code, 200)
#
#     def test_get_supplie_device(self):
#         sup = supply.Supply()
#         response = sup.get_supply_devices(21556, "ELECTRICITY")
#         self.assertEqual(response.status_code, 200)
#
#     def test_get_supplie_device_no_data(self):
#         sup = supply.Supply()
#         response = sup.get_supply_devices(21556, "WATER")
#         self.assertEqual(response.status_code, 204)  # No content
#
#     def test_get_supplie(self):
#         sup = supply.Supply()
#         response = sup.get_supply(21556, "ELECTRICITY")
#         self.assertEqual(response.status_code, 200)
