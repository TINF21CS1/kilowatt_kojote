from smartmeter.constants import URL_ENVIRONMENT
import requests as request_lib
from datetime import datetime

class requests:
    def get(attributes: list) -> list | object:
        result = list()
        for attribute in attributes:
            if(attribute == 'timestamp'):
                return datetime.today()
            response = request_lib.get(url=URL_ENVIRONMENT + '/' + attribute,)
            if(response.status_code == 200):
                result.append(response.json())
        return result if len(result) > 1 else result[0]