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
app.config["JWT_SECRET_KEY"] = ":@:$!!I'mN0tAp4ssw0rd:$!!:@"
jwt = JWTManager(app)


users = {
    "fede": {
        "username": "Federico",
        "password": generate_password_hash("fede1234"),
        "role": "user",
    },
    "holberton": {
        "username": "Holberton",
        "password": generate_password_hash("Holberton10647"),
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


@app.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.get("/jwt-protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)