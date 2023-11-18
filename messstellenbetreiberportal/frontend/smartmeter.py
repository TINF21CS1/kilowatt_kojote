from flask import (
    Blueprint, render_template, request,
)

from datetime import datetime
from .testdata import get_smartmeter_test_list
from .availability import uptime_smartmeters
from .errors import errors_smartmeter
#from ..backend.frontend import frontend_smartmeter_revoke, frontend_smartmeter, frontend_smartmeter_reading
import time
import logging

logger = logging.getLogger(__name__)

bp = Blueprint('smartmeter', __name__, url_prefix='/smartmeter')

@bp.route('', methods=['GET', 'POST'])
def smartmeter():
    if "id" in request.args:
        return detail()
    else:
        return overview()
    
def overview():
    if request.method == 'POST' and "id" in request.form:
        try:
            #frontend_smartmeter_revoke(request.form["id"])
            # TODO: Insert Revoke Functionality
            pass
        except ValueError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))

    try:
        smartmeters = get_smartmeter_test_list(100) # TODO: Change to real data
        #smartmeters = frontend_smartmeter()
    except ValueError as e:
        logger.exception(e)
        return render_template('error.html', errors=str(e))
    
    smartmeters = smartermeter_usage(smartmeters)

    return render_template('smartmeter/overview.html', smartmeters=smartmeters)

def detail():
    # Create list of smartmeters
    try:
        smartmeter = get_smartmeter_test_list(1) # TODO: Replace with real data
        #smartmeter = {
        #    "uuid" : request.args.get("id"),
        #    "data" : frontend_smartmeter_reading(request.args.get("id"))
        #}
    except ValueError as e:
        logger.exception(e)
        return render_template('error.html', errors=str(e))

    smartmeter = smartermeter_usage(smartmeter)

    # Get uptime for smartmeter
    current_time = int(time.time())
    uptime = uptime_smartmeters(smartmeter, current_time=current_time)

    # Define Plot Data 
    labels = [datetime.utcfromtimestamp(stamp).strftime('%Y-%m-%d %H:%M:%S') for stamp in uptime.keys()]
    data = list(uptime.values())
 
    # Return the components to the HTML template 
    return render_template(
        uuid=request.args.get("id"),
        data=data,
        labels=labels,
        template_name_or_list='smartmeter/detail.html',
        smartmeter=smartmeter[0],
        errors=errors_smartmeter(smartmeter),
        unix_to_datetime=unix_to_datetime,
        )

def unix_to_datetime(unix_time):
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')

# Expand smartmeter data with usage details
def smartermeter_usage(smartmeters:list) -> list:
    for smartmeter in smartmeters:
        for i, data in enumerate(smartmeter["data"]):
            # Check if previous list entry exists
            if len(smartmeter["data"]) > i+1:
                # Calculate usage
                data["usage"] = round((data["reading"] - smartmeter["data"][i+1]["reading"])*1000 / (data["timestamp"] - smartmeter["data"][i+1]["timestamp"]), 2)
    return smartmeters