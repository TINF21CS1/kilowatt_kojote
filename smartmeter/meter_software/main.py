import time

from .io import read_meter, read_buffer, write_buffer, read_config
from .network import requests

def main():
    current_reading = read_meter()
    datastore = read_buffer()
    data = {"timestamp": int(time.time()),
        "reading": current_reading}
    datastore.append(data)
    resp = requests.send(datastore)
    if(resp.status_code != 200):
        print("Request failed. Status code: " + str(resp.status_code))
        print(resp.content)
        write_buffer(datastore)

def register():
    config = read_config()
    register = {"type": config.get("type"),
            "latitude": config.get("latitude"),
            "longitude": config.get("longitude"),}
    print(register)
    while(requests.register(register).status_code != 200):
        time.sleep(5)