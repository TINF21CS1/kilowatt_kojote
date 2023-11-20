import os
import json
import time

from .constants import READING_FILE, BUFFER_FILE, CONFIG_FILE

def read_meter()->int:
    if os.path.isfile(READING_FILE):
        with open(READING_FILE, "r") as f:
            current = int(f.read())
        return current
    else:
        return 0

def read_buffer()->list:
    if os.path.isfile(BUFFER_FILE):
        with open(BUFFER_FILE, "r") as f:
            data = json.loads(f.read())
        return data
    else:
        return list()

def write_buffer(data:list)->None:
    with open(BUFFER_FILE, "w") as f:
        f.write(json.dumps(data))

def read_config()->dict:
    while not os.path.isfile(CONFIG_FILE):
        time.sleep(1)
    with open(CONFIG_FILE, "r") as f:
        data = json.loads(f.read())
    return data