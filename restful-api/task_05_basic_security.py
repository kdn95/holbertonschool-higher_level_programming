#!/usr/bin/python3
"""API Security Task 5"""
from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "Holberton"
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "User1": {
        "Sam":"user1",
        "password": generate_password_hash("hello"),
        "role": "user"
        },
        "admin1": {
            "username": "admin1",
            "password": generate_password_hash("hello"),
            "role": "admin"
        }
}


@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"


@app.route('/login', methods=["POST"])
def login():
    """Login"""
    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    for key in ["username", "password"]:
        if key not in data:
            abort(400, "Missing attr {}.".format(key))

    if data["username"] not in users or not check_password_hash(users[data["username"]]["password"], data["password"]):
        return jsonify({"message": "Incorrect username or password"}), 401
    
    access_token = create_access_token(identity=data["username"])
    return jsonify({"access_token": access_token})


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected", methods=["GET"])
@jwt_required
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required
def admin_only():
    current_usr = get_jwt_identity()
    
    if current_usr not in users or users[current_usr]["role"] != "admin":
        return jsonify({"error": "Admin access only"}), 403

    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
