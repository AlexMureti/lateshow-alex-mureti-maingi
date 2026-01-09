from flask import Blueprint,jsonify

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({"message": "Late show API is running"})