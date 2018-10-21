import requests

class Core:
    def __init__(host, token=None):
        self.host = host
        self._token = token
    
    @property
    def token(self):
        return self_token
    
    def repositories(self):
        NotImplemented
    
    def get_manifest(self, repo, reference):
        url = '{0}/v2/{1}/manifests/{2}'.format(self.host, repo, reference)
        return self._send_request_get(url)

    def _send_request_get(self, url):
        r = requests.get(url)
        status_code = r.status_code
        if status_code is not 200:
            raise DRCInvalidStatusCode()


class DRCException(Exception):
    """
    general class for exceptions
    """
    pass

class DRCInvalidStatusCode(DRCException):
    def __str__(self):
        return 'unvalid status code'