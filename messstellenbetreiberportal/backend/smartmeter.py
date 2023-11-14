from flask import Flask, request, jsonify, Blueprint
from .db import db_manager

bp = Blueprint("smartmeter_backend", __name__, url_prefix="/api/smartmeter")

@bp.route("/register", methods=["POST"])
def register():
    json = request.get_json()

    if not "type" in json or type(reader_type := json["type"]) != int:
        return "", 400

    sim_uuid = "test"

    db_manager.smartmeter_register(sim_uuid, reader_type)
    
    return jsonify(["test", 2, True])

@bp.route("/data", methods=["POST"])
def data():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])
