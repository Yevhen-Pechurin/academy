import logging
import requests

_logger = logging.getLogger(__name__)

BASE_URL = 'http://api.ipstack.com/'
ACCESS_KEY = '78fc7fe17f72e5974977cabdf4716e63'

class IpstackAPI(object):

    def __init__(self, key, base_url=BASE_URL, timeout=10):
        self.base_url = base_url
        self.key = key
        self.timeout = timeout

    def request_ip_data(self, ip):
        get_request_url = self.url_concat(self.base_url, ip)
        params = {'access_key': self.key}
        _logger.info('Sending request to Ipstack on url %s with param: \n%s' % (get_request_url, params))
        response = requests.get(get_request_url, params=params, timeout=self.timeout)
        response.raise_for_status()
        result = response.json()
        _logger.info('Received response from Ipstack: %s' % result)
        return result

    def url_concat(self, *args):
        arguments = [argument.strip('/ ') for argument in args]
        return '/'.join(arguments)


if __name__ == '__main__':
    api = IpstackAPI(ACCESS_KEY)
    api.request_ip_data('94.176.199.59')