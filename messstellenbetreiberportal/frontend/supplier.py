from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)
import logging
from ..backend.frontend import frontend_supplier_add, frontend_supplier_assign, frontend_supplier, frontend_smartmeter, JSONValidationError

logger = logging.getLogger(__name__)

bp = Blueprint('supplier', __name__, url_prefix='/supplier')

@bp.route('', methods=['GET'])
def supplier():
    return render_template(
        template_name_or_list='supplier/overview.html',
        suppliers=frontend_supplier())

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        notes = request.form['notes']
        
        try: 
            frontend_supplier_add({"name": name, "notes": notes})
        except JSONValidationError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))
        
        return redirect(url_for('supplier.supplier'))
    
    return render_template('supplier/add.html')

@bp.route('/assign', methods=['GET', 'POST'])
def assign():
    if request.method == 'POST':
        smartmeter_uuid = request.form['smartmeter']
        supplier_uuid = request.form['supplier']
        
        try:
            frontend_supplier_assign({"uuid":supplier_uuid, "smartmeter":smartmeter_uuid})
        except JSONValidationError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))
        
        return redirect(url_for('supplier.supplier'))
    
    else:
        try:
            smartmeters = frontend_smartmeter()
            suppliers = frontend_supplier()
        except JSONValidationError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))

        return render_template(
            suppliers = suppliers,
            smartmeters = smartmeters,
            template_name_or_list='supplier/assign.html')