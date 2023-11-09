from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('smartmeter', __name__, url_prefix='/smartmeter')

@bp.route('', methods=['GET', 'POST'])
def smartmeter():
    if "id" in request.args:
        return detail()
    else:
        return overview()
    
def overview():
    if request.method == 'POST' and "id" in request.form:
        # TODO: Insert Revoke Functionality
        pass

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
    # Define Plot Data 
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
    ]
 
    data = [0, 10, 15, 8, 22, 18, 25]
    return render_template(
        uuid=request.args.get("id"),
        data=data,
        labels=labels,
        template_name_or_list='smartmeter/detail.html')
    
