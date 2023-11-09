from flask import Flask, request, jsonify, Blueprint

bp = Blueprint("frontend_backend", __name__, url_prefix="/api/frontend")

@bp.route("/smartmeter", methods=["GET"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/smartmeter/reading", methods=["GET"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/smartmeter/usage", methods=["GET"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/smartmeter/revoke", methods=["POST"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/smartmeter/supplier", methods=["GET"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/supplier", methods=["GET"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/supplier/smartmeter", methods=["GET"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/supplier/add", methods=["POST"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])

@bp.route("/supplier/assign", methods=["POST"])
def register():
    json = request.get_json()
    print(json)
    return jsonify(["test", 2, True])
