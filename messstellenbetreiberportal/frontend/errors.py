from .availability import get_duration_downtime, INTERVAL
from datetime import datetime

def dowtime_error(smartmeter:dict, interval:int = INTERVAL) -> list:
    """Calculates the errors of a smartmeter.

    Args:
        smartmeter (dict): Smartmeter

    Returns:
        list(dict): Errors (uuid, timestamp, duration)
    """

    # Get the last reading
    last_reading = smartmeter['data'][-1]
    downtime = get_duration_downtime(last_reading)

    # Check if the last reading is older than the interval
    if downtime > interval:
        return [{
            'uuid': smartmeter['uuid'],
            'timestamp': datetime.utcfromtimestamp(last_reading['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
            'message': f'Zähler sendet seit {datetime.timedelta(seconds=downtime)} keine Daten!'
        }]
    else:
        return []
    
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

def errors_smartmeter(smartmeter:list, interval:int = INTERVAL) -> list:
    """Calculates the errors of a list of smartmeters.

    Args:
        smartmeter (list): List of smartmeters

    Returns:
        list(dict): List of errors (uuid, timestamp, message)
    """

    # Get the errors for each smartmeter
    errors = []
    for meter in smartmeter:
        errors += dowtime_error(meter)
        errors += backwards_reading_error(meter)

    return errors