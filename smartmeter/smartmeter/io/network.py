from smartmeter.constants import URL_ENVIRONMENT
import requests as request_lib

class requests:
    def get(attributes: list) -> list | any:
        result = list()
        for attribute in attributes:
            response = request_lib.get(url=URL_ENVIRONMENT + '/' + attribute,)
            if(response.status_code == 200):
                result.append(response.json())
        return result if len(result) > 1 else result[0]