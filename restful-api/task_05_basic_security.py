#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)

auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "kL9f$0P!2h6*GzB#7fPqW8qjXn@eTzR1"
jwt = JWTManager(app)

@jwt.unauthorized_loader
def handle_missing_token(error):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(error):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token(error):
    return jsonify({"error": "Fresh token required"}), 401



users = {
    "User1": {
        "username": "Gaston",
        "password": generate_password_hash("123gast11"),
        "role": "user",
    },
    "User2": {
        "username": "Holberton",
        "password": generate_password_hash("holberton87456"),
        "role": "admin",
    },
}


@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized"}), 401


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user is None:
        return None
    if check_password_hash(user["password"], password):
        return user


@app.get("/basic-protected")
@auth.login_required
def basic_auth():
    return f"Basic Auth: Access Granted"

@app.get("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    role = claims.get("role")
    if role != "admin":
        return jsonify({"error": "admin access required"}), 403
    return "admin access: granted"


@app.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify(access_token=access_token)


@app.get("/jwt-protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)