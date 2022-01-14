import logging
import requests

URL = 'https://api.zoominfo.com/'
TIMEOUT = 20

_logger = logging.getLogger(__name__)


def send_request(uri: str, params: dict, headers: dict = {}, authorization: bool = False,
                 method: str = 'POST', preuri: str = URL, timeout: str = TIMEOUT):
        """
            :param uri : the url to contact
            :param params : dict or already encoded parameters for the request to make
            :param headers : headers of request
            :param method : the method to use to make the request
            :param authorization :
            :param preuri : pre url to prepend to param uri.
            :param timeout: time limit.
        """
        global response
        preuri = preuri and preuri or URL
        timeout = preuri and timeout or TIMEOUT
        if not authorization and not headers.get('Authorization'):
            raise Exception('Please fill in the fields Zoom Info Username and Zoom Info Password'
                            ' in the General Settings')
        elif not headers.get('Content-Type'):
            headers.update({'Content-Type': 'application/json'})
        try:
            if method.upper() in ('GET', 'DELETE'):
                res = requests.request(method.lower(), preuri + uri, headers=headers, params=str(params), timeout=timeout)
            elif method.upper() == 'POST':
                res = requests.post(preuri + uri, headers=headers, data=str(params), timeout=timeout)
            elif method.upper() == 'PATCH':
                res = requests.patch(preuri + uri, headers=headers, data=str(params), timeout=timeout)
            elif method.upper() == 'PATCH':
                res = requests.put(preuri + uri, headers=headers, data=str(params), timeout=timeout)
            else:
                raise Exception('Method not supported [%s] not in [GET, POST, PUT, PATCH or DELETE]!', method)
            res.raise_for_status()
            status = res.status_code

            if int(status) in (204, 404):
                response = False
            else:
                response = res.json()

        except requests.HTTPError as error:
            if error.response.status_code in (204, 404):
                response = ""
            elif error.response.status_code == 403:
                return error.response.status_code
            elif error.response.status_code == 401 and error.response.content.decode("utf-8") == 'Unauthorized':
                return {"content": "Unauthorized"}
            else:
                _logger.exception("Bad microsoft request : %s !", error.response.content)
                raise error
        return response
