import logging

import logging
import requests

_loger = logging.getLogger(__name__)

URL = "http://api.ipstack.com/"


class IpStackApi(object):
    def __init__(self, key, url=URL):
        self.url = url
        self.key = key

    def join_url(self, *kw):
        res = ''
        for i in kw:
            start, end = 0, -1
            if i[start] == '/':
                start = 1
            if i[end] == '/':
                res += i[start:-1] + '/'
            else:
                res += i[start:] + '/'
        return res

    def get_data(self, ip):
        if self.url and ip:
            url = self.join_url(self.url, ip)
            data = requests.get(url, params={'access_key': self.key}, timeout=20)
            return data.json()


if __name__ == '__main__':
    api = IpStackApi('83277ff56052fff11a7d3d8313edbcb4')
    print(api.get_data('196.149.84.40'))
