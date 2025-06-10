
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return "API RESTful funcionando", 200

@app.route('/status')
def status():
    return jsonify({"status": "ok"}), 200

@app.route('/data')
def data():
    return jsonify({"users": users}), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Falta el nombre de usuario"}), 400
    if username in users:
        return jsonify({"error": "El usuario ya existe"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "Usuario agregado con éxito",
        "user": users[username]
    }), 201

@app.route('/users/<username>')
def get_user(username):
    if username not in users:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"user": users[username]}), 200
