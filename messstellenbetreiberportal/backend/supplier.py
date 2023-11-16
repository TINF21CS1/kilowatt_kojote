from flask import Flask, request, jsonify, Blueprint
from .db import db_manager
import jsonschema

bp = Blueprint("supplier_backend", __name__, url_prefix="/api/supplier")

serial_number_schema = {
    "type": "string",
    "minLength": 1
}

@bp.route("/reading/history", methods=["GET"])
def reading_history():
    
    serial_number = request.args.get("id")

    try:
        jsonschema.validate(serial_number, serial_number_schema)
    except jsonschema.ValidationError:
        return "", 400

    sn = request.headers.get("X-Serialnumber")

    if not db_manager.check_supplier_owns_reader(sn, serial_number):
        return "", 403

    return db_manager.supplier_reading_history(serial_number)    #TODO: An der stelle checken, wie der rückgabewert aussieht, es ist bestimmt kein dict in der liste, da muss ich vllt ne list/dict-comprehension machen

@bp.route("/reading/current", methods=["GET"])
def reading_current():
    
    serial_number = request.args.get("id")

    try:
        jsonschema.validate(serial_number, serial_number_schema)
    except jsonschema.ValidationError:
        return "", 400

    sim_supplier_id = "abc"

    if not db_manager.check_supplier_owns_reader(sim_supplier_id, serial_number):
        return "", 403

    return db_manager.supplier_reading_current(serial_number)   # TODO: Auch hier schauen, wie der rückgabewert der db aussieht. bestimmt kein dict

@bp.route("/smartmeter", methods=["GET"])
def smartmeter():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])
