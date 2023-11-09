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
    return render_template('supplier/add.html')