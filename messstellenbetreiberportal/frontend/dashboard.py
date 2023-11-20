from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('dashboard', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def dashboard():
    return render_template('smartmeter/dashboard.html')