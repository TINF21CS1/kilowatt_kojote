from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('smartmeter', __name__, url_prefix='/smartmeter')

@bp.route('', methods=['GET'])
def overview():
    if "id" in request.args:
        pass
    else:
        pass
    return render_template('smartmeter/overview.html')