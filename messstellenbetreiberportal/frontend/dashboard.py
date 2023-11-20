from flask import (
    Blueprint, render_template,
)

from datetime import datetime
from .availability import uptime_smartmeters
from .errors import errors_smartmeter
import time
import logging
from ..backend.frontend import frontend_smartmeter, JSONValidationError
from .smartmeter import smartermeter_usage

logger = logging.getLogger(__name__)

bp = Blueprint('dashboard', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def dashboard():
    # Create list of smartmeters
    try:
        smartmeters = frontend_smartmeter()
    except JSONValidationError as e:
        logger.exception(e)
        return render_template('error.html', errors=str(e))

    # Get uptime for all smartmeters
    current_time = int(time.time())
    uptime = uptime_smartmeters(smartmeters, current_time=current_time)

    # Get average uptime for last 24 hours
    day_interval = 60*60*24
    last_24_hour_uptime = {key: value for key, value in uptime.items() if key >= current_time-day_interval}
    average_uptime = sum(last_24_hour_uptime.values()) / len(last_24_hour_uptime) if len(last_24_hour_uptime) > 0 else 0

    # Get current usage and avg 24 usage
    smartmeters = smartermeter_usage(smartmeters)
    current_usages = []
    for smartmeter in smartmeters:
        if len(smartmeter["data"]) > 1:
            current_usages.append(smartmeter["data"][0]["usage"])

    avgerage_current_usage = sum(current_usages) / len(current_usages) if current_usages else 0

    # Location Data from string
    for smartmeter in smartmeters:
        smartmeter['location'] = [smartmeter["latitude"], smartmeter["longitude"]]

    # Define Plot Data 
    labels = [datetime.utcfromtimestamp(stamp).strftime('%Y-%m-%d %H:%M:%S') for stamp in uptime.keys()]
    data = list(uptime.values())
 
    # Return the components to the HTML template 
    return render_template(
        template_name_or_list='smartmeter/dashboard.html',
        data=data,
        labels=labels,
        current_uptime = round(data[-1]*100, 2) if data else 0,
        average_uptime = round(average_uptime*100, 2),
        smartmeters=smartmeters,
        errors=errors_smartmeter(smartmeters),
        usage=avgerage_current_usage
    )