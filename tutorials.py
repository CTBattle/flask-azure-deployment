# tutorials.py

from flask import Blueprint, request, jsonify

tutorials_bp = Blueprint("tutorials", __name__, url_prefix="/api/tutorials")

# In-memory list to simulate a database
tutorials = []

@tutorials_bp.route("/", methods=["GET"])
def get_tutorials():
    return jsonify(tutorials)

@tutorials_bp.route("/", methods=["POST"])
def create_tutorial():
    data = request.get_json()
    tutorials.append(data)
    return jsonify(data), 201
