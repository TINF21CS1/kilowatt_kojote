
from smartmeter.constants import READING_FILE

def write_reading(reading:int)->None:
    with open(READING_FILE, "w") as f:
        f.write(reading)