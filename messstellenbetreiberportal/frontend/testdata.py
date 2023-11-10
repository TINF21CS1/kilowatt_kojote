import string
import random
import time
from .availability import TIMEFRAME

def get_smartmeter_test_list(n:int):
    return [smartmeter for smartmeter in generate_smartmeters(n)]

def generate_readings(n):
    for _ in range(n):
        yield {
            "timestamp": random.randint(int(time.time()) - TIMEFRAME, int(time.time())),
            "reading": random.randint(100000, 200000)
        }

def generate_list_of_readings(n):
    return [reading for reading in generate_readings(n)]


def generate_smartmeters(n):
    for _ in range(n):
        yield {
            "uuid": generate_random_string(36),
            "type": random.randint(0, 2),
            "location": f"{random.uniform(47.754, 53.392)}, {random.uniform(07.071, 14.256)}",
            "supplier": generate_random_string(12),
            "data": generate_list_of_readings(random.randint(900, 1000))
        }

def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

# Print some example data
if __name__ == "__main__":
    print(get_smartmeter_test_list(10))