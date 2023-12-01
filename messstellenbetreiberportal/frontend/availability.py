import time
from collections import OrderedDict
import logging

logger = logging.getLogger('waitress')

INTERVAL = 60*15 # 15 minutes
TIMEFRAME = 60*60*24*30 # 30 days

def get_uptime(readings:list, interval:int = INTERVAL, timeframe:int = TIMEFRAME, current_time = int(time.time())) -> dict:
    """Calculates the uptime of a smartmeter from a list of readings.

    Args:
        readings (list): List of readings

    Returns:
        dict(int, int): Dictionary with the uptime for each interval
    """

    if len(readings) == 0:
        logger.warning(f"Did not receive any reading for uptime calculation. Returning default. (Current time: 0)")
        return {current_time: 0}

    # Iterate through the whole timeframe in intervals of 15 minutes and calculate the uptime
    uptime = OrderedDict()
    for i in range(current_time - timeframe, current_time, interval):
        # Check if there is a reading in the current interval
        if any(reading['timestamp'] >= i and reading['timestamp'] < i + interval for reading in readings):
            uptime[i] = 1
        else:
            uptime[i] = 0

    logger.info(f"Calculated uptime over last {TIMEFRAME} seconds. ({len(uptime)} values)")
    return uptime

def uptime_smartmeters(smartmeter:list, interval:int = INTERVAL, timeframe:int = TIMEFRAME, current_time:int = int(time.time())) -> dict:
    """Calculates the uptime of a list of smartmeters.

    Args:
        smartmeter (list): List of smartmeters

    Returns:
        dict(int, float): Dictionary with the uptime for each interval
    """

    if not smartmeter:
        logger.info("Did not receive any smartmeters! Returning empty dict for uptime!")
        return {}

    # Get the uptime for each smartmeter
    uptime = OrderedDict()
    for meter in smartmeter:
        uptime[meter['uuid']] = get_uptime(meter['data'], interval, timeframe, current_time)

    # Get average uptime for each interval
    average_uptime = OrderedDict()
    for i in uptime[smartmeter[0]['uuid']].keys():
        uptime_for_this_timestamp = [uptime[meter['uuid']][i] for meter in smartmeter if i in uptime[meter['uuid']]]
        if uptime_for_this_timestamp:
            average_uptime[i] = sum(uptime_for_this_timestamp) / len(uptime_for_this_timestamp)
        else:
            logger.warning(f"Uptime for timestamp {i} did not return anything. The average defaults to 0... This is highly unlikely and should be investigated!")
            average_uptime[i] = 0

    return average_uptime