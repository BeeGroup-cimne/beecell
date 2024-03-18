# from src.dexma import parameter
# from unittest import TestCase
#
#
# class ParametersTest(TestCase):
#
#     def test_get_parameters_without_params(self):
#         par = parameter.Parameter()
#         params = {}
#         response = par.get_parameters(1043036, params)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(type(response.json()), list)
#
#     def test_get_parameters(self):
#         par = parameter.Parameter()
#         params = {"start": 0, "limit": 20}
#         response = par.get_parameters(1043036, params)
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(type(response.json()), list)
#
#     def test_get_parameters_invalid_device(self):
#         par = parameter.Parameter()
#         params = {"start": 0, "limit": 20}
#         response = par.get_parameters('asdasd', params)
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(response.json()["message"], "Bad Request")
#
#     def test_get_parameters_no_exist_device(self):
#         par = parameter.Parameter()
#         params = {"start": 0, "limit": 20}
#         response = par.get_parameters(222222222, params)
#         self.assertEqual(response.status_code, 403)
#         self.assertEqual(response.json()["message"], "Entity not found")
#
#     def test_get_resolutions_no_data(self):
#         par = parameter.Parameter()
#         params = {"from_": "2020-01-01T00:00:00",
#                   "to_": "2021-01-01T00:00:00"}
#         response = par.get_resolutions(1043036, params)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], 'Not Found')
#
#     def test_get_resolutions_no_data2(self):
#         par = parameter.Parameter()
#         response = par.get_resolutions(1043036, {})
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(response.json()["message"], 'Not Found')
#
#     # TO DO find device_id with resolutions
#
#     '''
#     def test_get_resolutions(self):
#         par = parameter.Parameter()
#         params = {"from_": "2018-03-12",
#                   "to_": "2022-01-12"}
#         response = par.get_resolutions(1043036, params)
#         self.assertEqual(response.status_code, 200)  # 404
#     '''
