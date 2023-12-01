from flask import (
    Blueprint, redirect, render_template, request, session, url_for, send_file
)
import logging
from io import BytesIO
import base64
from ..backend.frontend import frontend_supplier_add, frontend_supplier_assign, frontend_supplier, frontend_smartmeter, JSONValidationError

logger = logging.getLogger('waitress')

bp = Blueprint('supplier', __name__, url_prefix='/supplier')

@bp.route('', methods=['GET'])
def supplier():
    return render_template(
        template_name_or_list='supplier/overview.html',
        suppliers=frontend_supplier())

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST' and "name" in request.form and "notes" in request.form:
        logger.info(f"Received POST on /add (Name: {request.form['name']}, Notes: {request.form['notes']}). Adding new supplier...")
        name = request.form['name']
        notes = request.form['notes']
        
        try: 
            dict = frontend_supplier_add({"name": name, "notes": notes})
            cert = base64.b64decode(dict["certificate"])
        except JSONValidationError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))
        
        buffer = BytesIO()
        buffer.write(cert)
        buffer.seek(0)

        logger.info(f"Initiating Certificate Download")
        return send_file(
            buffer,
            as_attachment=True,
            download_name='cert.pfx',
            mimetype='application/x-pkcs12'
        )
    
    return render_template('supplier/add.html')

@bp.route('/assign', methods=['GET', 'POST'])
def assign():
    if request.method == 'POST' and "smartmeter" in request.form and "supplier" in request.form:
        logger.info(f"Received POST on /assign (Smartmeter UUID: {request.form['smartmeter']}, Supplier UUID: {request.form['supplier']}). Assigning supplier to smartmeter...")
        smartmeter_uuid = request.form['smartmeter']
        supplier_uuid = request.form['supplier']
        
        try:
            frontend_supplier_assign({"uuid":supplier_uuid, "smartmeter":smartmeter_uuid})
        except JSONValidationError as e:
            logger.exception(e)
            return render_template('error.html', errors=str(e))
        
        logger.info(f"Assigning successful. Redirecting...")
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
