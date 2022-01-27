import logging
import requests


URL = 'http://api.ipstack.com/'

_logger = logging.getLogger(__name__)


class IpstackApi(object):

    def __init__(self, key, url=URL, timeout=10):
        self.url = url
        self.key = key
        self.timeout = timeout

    def get_ip_data(self, ip):
        url = self.join_url(self.url) + ip
        params = {'access_key': self.key }
        _logger.info('Send request to ipstack on url %s and param: \n%s' % (url, params))
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        result = response.json()
        _logger.info('Received response from ipstack: %s' % result)

        return result

    def join_url(self, *urls):
        result = ""
        for url in urls:
            if url[-1] != '/':
                url += '/'
            elif url[0] == '/':
                url = url[1:]
            result += url

        return result


if __name__ == "__main__":
    api = IpstackApi('faa1d586190e807e4a46cdc4d0ced040')
    print(api.get_ip_data('94.176.199.59'))
