import requests as request_lib

from .constants import URL, URL_REGISTER, URL_DATA, CERT

class requests:
    def register(data):
        return request_lib.post(url=URL+URL_REGISTER, data=data, cert=CERT)

    def send(data):
        return request_lib.post(url=URL+URL_DATA, data=data, cert=CERT)