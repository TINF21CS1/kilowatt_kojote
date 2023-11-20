import os
import json

from .constants import READING_FILE, BUFFER_FILE

def read_meter()->int:
    if os.path.exists(READING_FILE):
        with open(READING_FILE, "r") as f:
            current = int(f.read())
        return current
    else:
        return 0

def read_buffer()->list:
    if os.path.exists(BUFFER_FILE):
        with open(BUFFER_FILE, "r") as f:
            data = json.loads(f.read())
        return data
    else:
        return list()

def write_buffer(data:list)->None:
    with open(BUFFER_FILE, "w") as f:
        f.write(json.dumps(data))