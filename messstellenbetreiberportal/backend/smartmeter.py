from flask import Flask, request, jsonify, Blueprint
from .db import db_manager
import jsonschema
import time

bp = Blueprint("smartmeter_backend", __name__, url_prefix="/api/smartmeter")

smartmeter_register_schema = {
    "type": "object",
    "properties": {
        "type": {
            "description": "Type of the smartmeter",
            "type": "integer",
            "minimum": 0,
            "maximum": 3
        },
        "latitude": {
            "description": "Latitude of the smartmeter",
            "type": "number",
            "minimum": -90,
            "maximum": 90,
        },
        "longitude": {
            "description": "Longitude of the smartmeter",
            "type": "number",
            "minimum": -180,
            "maximum": 180,
        }
    },
    "required": ["type", "latitude", "longitude"]
}

smartmeter_data_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "timestamp": {
                "description": "Timestamp of the submitted reading",
                "type": "integer",
                "minimum": 0
            },
            "reading": {
                "description": "The reading of the reader at the timestamp",
                "type": "integer"
            }
        },
        "required": ["timestamp", "reading"]
    },
    "minItems": 1
}

@bp.route("/register", methods=["POST"])
def register():
    json = request.get_json()

    try:
        jsonschema.validate(json, smartmeter_register_schema)
    except jsonschema.ValidationError as e:
        print(e)
        return "", 400

    sn = request.headers.get("X-Serialnumber")

    db_manager.smartmeter_register(sn, json["type"], round(json["latitude"], 5), round(json["longitude"], 5))
    
    return ""

@bp.route("/data", methods=["POST"])
def data():
    json = request.get_json()
    
    try:
        jsonschema.validate(json, smartmeter_data_schema)
    except jsonschema.ValidationError as e:
        print(e)
        return "", 400

    sn = request.headers.get("X-Serialnumber")

    actual_timestamp = int(time.time())

    for element in json:
        db_manager.smartmeter_data(sn, element["timestamp"], actual_timestamp, element["reading"])

    return ""