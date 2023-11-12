from flask import Flask, request, jsonify, Blueprint
from .db import db_manager

bp = Blueprint("supplier_backend", __name__, url_prefix="/api/supplier")

@bp.route("/reading/history", methods=["GET"])
def reading_history():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/reading/current", methods=["GET"])
def reading_current():
    #json = request.get_json()
    #print(json)
    return jsonify(["test", 2, True])

@bp.route("/usage/history", methods=["GET"])
def usage_history():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/usage/current", methods=["GET"])
def usage_current():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/smartmeter", methods=["GET"])
def smartmeter():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])
