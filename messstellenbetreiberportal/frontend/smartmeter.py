from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('smartmeter', __name__, url_prefix='/smartmeter')

@bp.route('', methods=['GET'])
def smartmeter():
    if "id" in request.args:
        return detail()
    else:
        return overview()
    
def overview():
    # Random input for testing smartmeter overview
    smartmeters = [
        {
            "uuid": "123456789012sgf34567890123456789012",
            "type": "Smartmeter",
            "location": "Keller",
            "supplier": "Stadtwerke",
            "reading": "1234567890",
            "usage": "1234567890",
            "avg_usage": "1234567890"
        },
        {
            "uuid": "23452345",
            "type": "Smartmeter",
            "location": "Keller",
            "supplier": "LOLOL",
            "reading": "1234567890",
            "usage": "1234567890",
            "avg_usage": "1234567890"
        },
        {
            "uuid": "qwerqwerqwer",
            "type": "Smartmeter",
            "location": "Keller",
            "supplier": "LOLOL",
            "reading": "1234567890",
            "usage": "1234567890",
            "avg_usage": "1234567890"
        },
    ]


    return render_template('smartmeter/overview.html', smartmeters=smartmeters*100)

def detail():
    return render_template('smartmeter/detail.html')
    
