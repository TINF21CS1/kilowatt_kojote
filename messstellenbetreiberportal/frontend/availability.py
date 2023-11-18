import time
from collections import OrderedDict

INTERVAL = 60*15 # 15 minutes
TIMEFRAME = 60*60*24*30 # 30 days

def get_duration_downtime(last_reading:dict, current_time = int(time.time())) -> int:
    """Calculates the duration of a downtime from a reading.
    """

    downtime = current_time - last_reading['timestamp']

    return downtime

def get_uptime(readings:list, interval:int = INTERVAL, timeframe:int = TIMEFRAME, current_time = int(time.time())) -> dict:
    """Calculates the uptime of a smartmeter from a list of readings.

    Args:
        readings (list): List of readings

    Returns:
        dict(int, int): Dictionary with the uptime for each interval
    """

    if len(readings) == 0:
        return [1]

    # Iterate through the whole timeframe in intervals of 15 minutes and calculate the uptime
    uptime = OrderedDict()
    for i in range(current_time - timeframe, current_time, interval):
        # Check if there is a reading in the current interval
        if any(reading['timestamp'] >= i and reading['timestamp'] < i + interval for reading in readings):
            uptime[i] = 1
        else:
            uptime[i] = 0

    return uptime

def uptime_smartmeters(smartmeter:list, interval:int = INTERVAL, timeframe:int = TIMEFRAME, current_time:int = int(time.time())) -> dict:
    """Calculates the uptime of a list of smartmeters.

    Args:
        smartmeter (list): List of smartmeters

    Returns:
        dict(int, float): Dictionary with the uptime for each interval
    """

    # Get the uptime for each smartmeter
    uptime = OrderedDict()
    for meter in smartmeter:
        uptime[meter['uuid']] = get_uptime(meter['data'], interval, timeframe, current_time)

    # Get average uptime for each interval
    average_uptime = OrderedDict()
    for i in range(current_time - timeframe, current_time, interval):
        average_uptime[i] = sum(uptime[meter['uuid']][i] for meter in smartmeter) / len(smartmeter)

    return average_uptime

# Print some example data
if __name__ == "__main__":
    from testdata import get_smartmeter_test_list
    smartmeters = get_smartmeter_test_list(10)
    print(uptime_smartmeters(smartmeters))