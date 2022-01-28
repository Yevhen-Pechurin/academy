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


    def join_url(self, *args, sep="/"):
        url_list = []
        for url in args:
            if url[0] == sep:
                url = url[1:]
            if url[-1] == sep:
                url = url[:-1]
            url_list.append(url)
        return sep.join(url_list)


    # def join_url(self, *args):
    #     return "/".join(arg.strip("/") for arg in args)

    # def join_url(self, *args):
    #     arguments = [argument.strip("/ ") for argument in args]
    #     return "/".join(arguments)


if __name__ == "__main__":
    api = IpstackApi('eb7728351239287e12c4710297a5dd4d')
    print(api.get_ip_data('46.219.214.231'))
