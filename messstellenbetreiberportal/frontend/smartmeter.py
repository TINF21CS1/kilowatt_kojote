from flask import (
    Blueprint, render_template, request,
)

from datetime import datetime
from .availability import uptime_smartmeters
from .errors import errors_smartmeter
from ..backend.frontend import frontend_smartmeter_revoke, frontend_smartmeter, frontend_smartmeter_reading, JSONValidationError
import time
import logging

logger = logging.getLogger('waitress')

bp = Blueprint('smartmeter', __name__, url_prefix='/smartmeter')

@bp.route('', methods=['GET', 'POST'])
def smartmeter():
    if "id" in request.args:
        return detail()
    else:
        return overview()
    
def overview():
    if request.method == 'POST' and "id" in request.form:
        logger.info(f"Received POST on /smartmeter for revocation (ID: {request.form['id']}). Revoking smartmeter...")
        try:
            frontend_smartmeter_revoke(request.form["id"])
        except JSONValidationError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))
        logger.info(f"Revocation successful")

    try:
        smartmeters = frontend_smartmeter()
    except JSONValidationError as e:
        logger.exception(e)
        return render_template('error.html', errors=str(e))
    
    smartmeters = smartermeter_usage(smartmeters)

    type_translator = {
        0: "Wohnhaus", 
        1: "Industrie", 
        2: "Einspeisung", 
        3: "Einspeisung Wohnhaus"
    }

    return render_template('smartmeter/overview.html', smartmeters=smartmeters, type_translator=type_translator)

def detail():
    # Create list of smartmeters
    try:
        logger.info(f"Requesting smartmeter detail data. (Args: {request.args})")
        smartmeter = [next(smartmeter for smartmeter in frontend_smartmeter() if smartmeter["uuid"] == request.args.get("id"))]
    except (JSONValidationError, StopIteration) as e:
        logger.exception(e)
        return render_template('error.html', errors=str(e))

    logger.info(f"Calculating usage information and errors for smartmeter: {smartmeter[0]['uuid']}")
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
        sorted_data_list = sorted(smartmeter["data"], key=lambda x: x["timestamp"])
        for i, data in enumerate(sorted_data_list):
            # Check if previous list entry exists
            if len(smartmeter["data"]) > i+1:
                # Calculate usage
                data["usage"] = round((data["reading"] - smartmeter["data"][i+1]["reading"])*1000 / (data["timestamp"] - smartmeter["data"][i+1]["timestamp"]), 2) if data["timestamp"] - smartmeter["data"][i+1]["timestamp"] != 0 else "FEHLER"
            else:
                data["usage"] = 0
    return smartmeters