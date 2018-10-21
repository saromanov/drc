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
    
    def _send_request_get(self, url):
        r = requests.get(url)
        status_code = r.status_code
        if status_code is not 200:
            raise Exception("Unable to send get request")