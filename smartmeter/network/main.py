import requests as request_lib
from smartmeter.constants import URL, URL_REGISTER, URL_DATA

class requests:
    def register(data):
        return request_lib.post(url=URL+URL_REGISTER, data=data)

    def send(data):
        return request_lib.post(url=URL+URL_DATA, data=data)