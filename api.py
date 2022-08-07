import requests
import json


class Keitaro:

    def __init__(self, api_key, url, limit):
        self.limit = limit
        self.url = url
        self.api_key = api_key

    def query(self):
        query = {'limit': self.limit}
        return query

    def response(self):
        header = {'api-key': self.api_key}
        response = requests.post(self.url, headers=header, data=self.query())
        return response.text

    def get_exact(self):
        jn = self.response()
        loads = json.loads(jn)
        return loads['total']

    def get_sub(self):
        jn = self.response()
        loads = json.loads(jn)
        return loads['rows'][0]['sub_id_6']
