import requests

from dexma.decorator import dexma_parser


class Projects(object):
    url_fragment = '/mv/projects'

    def __init__(self, dexma):
        self.dexma = dexma
        self.url = self.dexma.base_url + self.url_fragment

    @dexma_parser
    def list_projects(self, params):
        response = requests.request(
            "GET",
            self.url,
            headers=self.dexma.headers,
            params=params)
        return response

    @dexma_parser
    def get_project(self, project_id ,params):
        url = f'{self.url}/{project_id}'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers,
            params=params)
        return response

    @dexma_parser
    def get_project_readings(self, project_id, params):
        url = f'{self.url}/{project_id}/readings'
        response = requests.request(
            "GET",
            url,
            headers=self.dexma.headers,
            params=params)
        return response
