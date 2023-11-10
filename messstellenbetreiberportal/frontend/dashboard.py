from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from datetime import datetime
from .testdata import get_smartmeter_test_list
from .availability import uptime_smartmeters, TIMEFRAME, INTERVAL
import time

bp = Blueprint('dashboard', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def dashboard():
    # Create list of smartmeters
    smartmeters = get_smartmeter_test_list(10)

    current_time = int(time.time())
    # Get uptime for all smartmeters
    uptime = uptime_smartmeters(smartmeters, current_time=current_time)

    # Average uptime over last 24 hours
    day_interval = 60*60*24
    
    # Get average uptime for last 24 hours
    last_24_hour_uptime = {key: value for key, value in uptime.items() if key >= current_time-day_interval}

    average_uptime = sum(last_24_hour_uptime.values()) / len(last_24_hour_uptime)

    # Define Plot Data 
    labels = [datetime.utcfromtimestamp(stamp).strftime('%Y-%m-%d %H:%M:%S') for stamp in uptime.keys()]
    data = list(uptime.values())
 
    # Return the components to the HTML template 
    return render_template(
        template_name_or_list='smartmeter/dashboard.html',
        data=data,
        labels=labels,
        current_uptime = round(data[-1], 4),
        average_uptime = round(average_uptime, 4),
    )
