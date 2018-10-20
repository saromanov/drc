import requests

class Core:
    def __init__(host, token=None):
        self.host = host
        self._token = token
    
    @property
    def token(self):
        return self_token