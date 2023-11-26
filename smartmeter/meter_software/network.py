import requests as request_lib

from .constants import URL, URL_REGISTER, URL_DATA, CERT_PEM, CERT_KEY

class requests:
    def register(data):
        return request_lib.post(url=URL+URL_REGISTER, json=data, cert=(CERT_PEM, CERT_KEY))

    def send(data):
        return request_lib.post(url=URL+URL_DATA, json=data, cert=(CERT_PEM, CERT_KEY))