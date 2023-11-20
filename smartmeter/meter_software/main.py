import time

from .io import read_meter, read_buffer, write_buffer, read_config
from .network import requests

def main():
    current_reading = read_meter()
    datastore = read_buffer()
    data = {"timestamp": time.time(),
        "reading": current_reading}
    datastore.append(data)
    if((response := requests.send(datastore)).status != '200'):
        write_buffer(datastore)

def register():
    config = read_config()
    register = {"type": config.get("type"),
            "location": config.get("location"),}
    while(requests.register(register).status != '200'):
        pass