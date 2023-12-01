from .availability import INTERVAL
from datetime import datetime, timedelta
import logging

logger = logging.getLogger('waitress')

def dowtime_error(smartmeter:dict, interval:int = INTERVAL) -> list:
    """Calculates the errors of a smartmeter.

    Args:
        smartmeter (dict): Smartmeter

    Returns:
        list(dict): Errors (uuid, timestamp, duration)
    """

    result = []

    for reading in smartmeter['data']:
        downtime = reading["actual_timestamp"] - reading["timestamp"]

        # Check if the last reading is older than the interval
        if abs(downtime) > interval:
            result.append({
                'uuid': smartmeter['uuid'],
                'timestamp': datetime.utcfromtimestamp(reading["actual_timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
                'message': f'Zähler sendet seit {timedelta(seconds=downtime)} keine Daten!'
            })
    
    return result
    
def backwards_reading_error(smartmeter:dict) -> list:
    """Checks if there is a backwards reading in a smartmeter.

    Args:
        smartmeter (dict): Smartmeter

    Returns:
        list(dict): Errors (uuid, timestamp, message)
    """

    # Get the readings
    readings = smartmeter['data']

    errors = []

    # Check if there is a backwards reading
    for i in range(1, len(readings)):
        if readings[i]['reading'] < readings[i-1]['reading'] and smartmeter['type'] != 2:
            errors.append({
                'uuid': smartmeter['uuid'],
                'timestamp': datetime.utcfromtimestamp(readings[i]['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                'message': f'Zählerstand ist rückläufig! Differenz: {readings[i-1]["reading"] - readings[i]["reading"]}'
            })

    return errors

def errors_smartmeter(smartmeter:list) -> list:
    """Calculates the errors of a list of smartmeters.

    Args:
        smartmeter (list): List of smartmeters

    Returns:
        list(dict): List of errors (uuid, timestamp, message)
    """

    # Get the errors for each smartmeter
    errors = []
    for meter in smartmeter:
        logger.info(f"Getting errors for smartmeter: {meter['uuid']}, type: {meter['type']}")
        errors += dowtime_error(meter)
        if meter["type"] not in [2,3]:
            errors += backwards_reading_error(meter)

        logger.info(f"Got errors: {errors}")
    return errors