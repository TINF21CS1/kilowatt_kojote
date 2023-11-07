from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('smartmeter', __name__, url_prefix='/smartmeter')

@bp.route('', methods=['GET'])
def overview():
    if "id" in request.args:
        return render_template('smartmeter/detail.html')
    else:
        return render_template('smartmeter/overview.html')
    
