from flask import Flask, request, jsonify, Blueprint

bp = Blueprint("smartmeter_backend", __name__, url_prefix="/api/smartmeter")

@bp.route("/register", methods=["POST", "GET"])
def register():
    return "registerd"