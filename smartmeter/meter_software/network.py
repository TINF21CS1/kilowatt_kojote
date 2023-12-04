import requests as request_lib

from .constants import URL, URL_REGISTER, URL_DATA, CERT_PEM, CERT_KEY

class requests:
    def register(data):
        response = request_lib.post(url=URL+URL_REGISTER, json=data, cert=(CERT_PEM, CERT_KEY))
        if(response.status_code == 200):
            print(f'Successfully registered Smartmeter \n URL: {URL+URL_REGISTER} \n Data: {data}')
        else:
            print(f'Error when registering Smartmeter \n URL: {URL+URL_REGISTER} \n Data: {data} \n Response: Code={response.status_code}\n Content={response.content}')
        return response

    def send(data):
        print(data)
        response = request_lib.post(url=URL+URL_DATA, json=data, cert=(CERT_PEM, CERT_KEY))
        if(response.status_code == 200):
            print(f'Successfully transmitted current reading \n URL: {URL+URL_DATA} \n Date: {data}')
        else:
            print(f'Error when transmitting current reading \n URL: {URL+URL_DATA} \n Data: {data} \n Response: Code={response.status_code}\n Content={response.content}')
        return response
