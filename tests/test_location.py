# from src.dexma import location
# from unittest import TestCase
#
#
# class LocationTest(TestCase):
#     # TO DO find a device_id with existing location
#     def test_get_locations(self):
#         params = {"device_id": 1043036}
#         loc = location.Location()
#         response = loc.get_locations(params)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], "Not Found")
#
#     def test_get_location(self):
#         loc = location.Location()
#         response = loc.get_location(25217)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], "Not Found")
#
#     def test_location_devices(self):
#         loc = location.Location()
#         response = loc.get_location_devices(25217)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], "Not Found")
#
#     def test_get_location_referenced_devices(self):
#         loc = location.Location()
#         response = loc.get_location_referenced_devices(25217)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], "Not Found")
#
#     def test_get_valid_activities(self):
#         loc = location.Location()
#         response = loc.get_valid_activities()
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], "Not Found")
