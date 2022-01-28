import logging
import requests

URL = "http://api.ipstack.com/"

_logger = logging.getLogger(__name__)


class IpStackAPI(object):

    def __init__(self, key, url=URL):
        self.url = url
        self.key = key

    def get_ip_data(self, ip):
        data = request
        return data


if __name__ == "__main__":
    api = IpStackAPI('f9f17c8a2e83b94a4dab3115b4d64698')
    print(api.get_ip_data('109.207.199.207'))
