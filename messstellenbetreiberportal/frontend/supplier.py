from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('supplier', __name__, url_prefix='/supplier')

@bp.route('', methods=['GET'])
def supplier():
    return render_template('supplier/overview.html')

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        street = request.form['notes']
        # TODO: Add code to add supplier to database
        return redirect(url_for('supplier.supplier'))
    
    return render_template('supplier/add.html')

@bp.route('/assign', methods=['GET', 'POST'])
def assign():
    if request.method == 'POST':
        smartmeter = request.form['smartmeter']
        supplier = request.form['supplier']
        # TODO: Add code to add assignment to database
        return redirect(url_for('supplier.supplier'))
    
    # Create list of smartmeters
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

    # Create list of suppliers
    suppliers = [
        {
            "uuid": "123456789012sgf34567890123456789012",
            "name": "Stadtwerke",
        },
        {
            "uuid": "23452345",
            "name": "LOLOL",
        },
        {
            "uuid": "qwerqwerqwer",
            "name": "LOLOL",
        }
    ]

    return render_template(
        suppliers = suppliers,
        smartmeters = smartmeters,
        template_name_or_list='supplier/assign.html')