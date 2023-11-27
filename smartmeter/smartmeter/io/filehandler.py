import json

from smartmeter.constants import READING_FILE, CONFIG_FILE

def write_reading(reading:int)->None:
    with open(READING_FILE, "w") as f:
        f.write(str(reading))

def write_config(type, latitude, longitude)->None:
    config = {"type": type,
            "latitude": latitude,
            "longitude": longitude,}
    with open(CONFIG_FILE, "w") as f:
            f.write(json.dumps(config))