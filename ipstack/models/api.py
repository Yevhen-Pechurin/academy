import logging
import requests

_logger = logging.getLogger(__name__)

URL = 'http://api.ipstack.com/'


class IpstackApi(object):

    def __init__(self, key, url=URL, timeout=10):
        self.url = url
        self.key = key
        self.timeout = timeout

    def get_ip_data(self, ip):
        url = self.join_url(self.url, ip)
        params = {'access_key': self.key}
        _logger.info('Send request to ipstack on url %s and param: \n%s' % (url, params))
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        result = response.json()
        _logger.info('Received response from ipstack: %s' % result)
        return result

    def join_url(self, *arg):
        return ''


if __name__ == "__main__":
    api = IpstackApi('246f192f9157fed2573ae98a901cd1a0')
    print(api.get_ip_data('94.176.199.59'))
