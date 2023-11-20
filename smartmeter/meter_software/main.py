import time

from .io import read_meter, read_buffer, write_buffer
from .network import requests

def main():
    current_reading = read_meter()
    datastore = read_buffer()
    data = {"timestamp": time.time(),
        "reading": current_reading}
    datastore.append(data)
    if((response := requests.send(datastore)).status != '200'):
        write_buffer(datastore)