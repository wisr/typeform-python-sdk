import urlparse

import requests


class Client(object):
    BASE_URL = 'https://api.typeform.com/v1/'

    def __init__(self, api_key):
        super(Client, self).__init__()

        self.api_key = api_key
        self._client = requests.Session()
        self._client.headers = {
            'User-Agent': 'python-typeform/0.1.0',
        }

    def _request(self, method, path, params=None):
        if params is None:
            params = dict()

        params['key'] = self.api_key
        url = urlparse.urljoin(self.BASE_URL, path)

        resp = self._client.request(method=method, url=url, params=params)

        # TODO: Raise an exception here
        if resp.status_code != 200:
            pass

        return resp.json()
