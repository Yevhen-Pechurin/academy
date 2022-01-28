import logging
import requests

_logger = logging.getLogger(__name__)


class IpStackAPI(object):

    def __init__(self, key, url=URL, timeout=10):
        self.url = url
        self.key = key
        self.timeout = timeout

    def get_ip_data(self, ip):
        url = self.join_url(self.url, ip)
        response = requests.get(url, params={'access_key': self.key}, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def join_url(self, *args):
        return "/".join(arg.strip("/") for arg in args)

if __name__ == "__main__":
    api = IpStackAPI('f9f17c8a2e83b94a4dab3115b4d64698')
    print(api.get_ip_data('109.207.199.207'))
