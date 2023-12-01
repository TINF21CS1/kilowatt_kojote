from flask import request, jsonify, Blueprint
from .db import db_manager
import jsonschema
import logging

bp = Blueprint("supplier_backend", __name__, url_prefix="/api/supplier")
logger = logging.getLogger(__name__)

serial_number_schema = {
    "type": "string",
    "minLength": 1
}

@bp.route("/reading/history", methods=["GET"])
def reading_history():
    
    serial_number = request.args.get("id")

    try:
        jsonschema.validate(serial_number, serial_number_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"Serial number(uuid) Validation failed at /supplier/history from Client at {request.remote_addr}:\n{e}")
        return "", 400

    sn = request.headers.get("X-Serialnumber")

    if not db_manager.check_supplier_owns_reader(sn, serial_number):
        return "", 403

    raw_output = db_manager.supplier_reading_history(serial_number)
    keys = ["timestamp", "reading"]

    return jsonify([dict(zip(keys, row)) for row in raw_output])

@bp.route("/reading/current", methods=["GET"])
def reading_current():
    
    serial_number = request.args.get("id")

    try:
        jsonschema.validate(serial_number, serial_number_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"Serial number(uuid) Validation failed at /supplier/current from Client at {request.remote_addr}:\n{e}")
        return "", 400

    sn = request.headers.get("X-Serialnumber")

    if not db_manager.check_supplier_owns_reader(sn, serial_number):
        return "", 403

    raw_output = db_manager.supplier_reading_current(serial_number)
    keys = ["timestamp", "reading"]

    return jsonify(dict(zip(keys, raw_output)))

@bp.route("/smartmeter", methods=["GET"])
def smartmeter():

    sn = request.headers.get("X-Serialnumber")
    sn = 1

    raw_output = db_manager.supplier_smartmeter(sn)
    logger.info(f"Called smartmeter: \n{raw_output}")
    keys = ["uuid", "type", "latitude", "longitude", "supplier"]

    return jsonify([dict(zip(keys, row)) for row in raw_output])
