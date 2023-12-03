import os
import json
import time

from .constants import READING_FILE, BUFFER_FILE, CONFIG_FILE

def read_meter()->int:
    with open(READING_FILE, "r") as f:
        current = int(float(f.read()))
    print(f'Current reading: {current} kWh')
    return current

def read_buffer()->list:
    if os.path.isfile(BUFFER_FILE):
        with open(BUFFER_FILE, "r") as f:
            data = json.loads(f.read())
        os.remove(BUFFER_FILE) 
        return data
    else:
        return list()

def write_buffer(data:list)->None:
    with open(BUFFER_FILE, "w") as f:
        f.write(json.dumps(data))
    print(f'Content stored for later transmission: {data}')

def read_config()->dict:
    waittime = 5
    while not os.path.isfile(CONFIG_FILE):
        print(f'Waiting {waittime} seconds for config to be loaded...')
        time.sleep(waittime)
    with open(CONFIG_FILE, "r") as f:
        data = json.loads(f.read())
    print(f'Configuration data was loaded successfully')
    return data