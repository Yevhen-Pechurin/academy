import logging
import requests

URL = 'https://api.zoominfo.com/'
TIMEOUT = 20

_logger = logging.getLogger(__name__)


class ZoomApi(object):

    def __init__(self, token=None, username=None, password=None, server_url=URL, timeout=TIMEOUT):
        self.server_url = server_url
        self.timeout = timeout
        self.username = username
        self.password = password
        self._token = token

    def get_authentification_token(self):
        params = {'username': self.username, 'password': self.password}
        response = self.send_request('authenticate', params)
        self._token = response['jwt']
        return self._token

    def authentication(self):
        self.get_authentification_token()

    def get_header(self):
        return self._token and {'Authorization': f"Bearer {self._token}"} or None

    def send_request(self, url: str, params: dict = None, method: str = 'POST') -> dict:
        """
            :param url : the url to contact
            :param params : dict or already encoded parameters for the request to make
            :param method : the method to use to make the request
        """
        headers = self.get_header()
        url = self.concat_url(self.server_url, url)
        _logger.info('send_request: Zoom Info send request on url %s with param: \n%s' % (url, params))
        res = requests.request(method, url=url, headers=headers,
                               json=params, timeout=self.timeout)
        if res.status_code == 401 and res.text == 'Unauthorized':
            return {'error': res.text}
        res.raise_for_status()
        data = res.json()
        _logger.info("send_request: Received data:\n%s", data)
        return data

    @staticmethod
    def concat_url(*args):
        new_url = ''
        for url in args:
            if url[0] == '/':
                url = url[1:]
            if url[-1] != '/':
                url += '/'
            new_url += url
        return new_url
