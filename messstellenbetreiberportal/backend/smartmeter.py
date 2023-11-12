from flask import Flask, request, jsonify, Blueprint
from .db import db_manager

bp = Blueprint("smartmeter_backend", __name__, url_prefix="/api/smartmeter")

@bp.route("/register", methods=["POST"])
def register():
    json = request.get_json()

    if not ("uuid" in json and "type" in json):
        return "", 404

    print(json)
    return jsonify(["test", 2, True])

@bp.route("/data", methods=["POST"])
def data():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])
