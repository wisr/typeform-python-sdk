import urlparse

import requests

from .errors import (NotAuthorizedException, NotFoundException, InvalidRequestException,
                     RateLimitException, UnknownException)


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

        if resp.status_code == 500:
            raise UnknownException('typeform client received 500 response from api')

        try:
            data = resp.json()
        except ValueError:
            raise UnknownException('typeform client could not decode json from response')

        if resp.status_code == 200:
            return data

        message = data.get('message')
        if resp.status_code == 404:
            raise NotFoundException(message)
        elif resp.status_code == 403:
            raise NotAuthorizedException(message)
        elif resp.status_code == 400:
            raise InvalidRequestException(message)
        elif resp.status_code == 429:
            raise RateLimitException(message)

        raise UnknownException(
            'typeform client received unknown response status code {code!r}'.format(code=resp.status_code)
        )
