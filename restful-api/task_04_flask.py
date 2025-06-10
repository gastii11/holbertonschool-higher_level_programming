#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"nombre": "Jane", "age": 28, "ciudad": "Los Angeles"},
    }

@app.route('/')
def home():
    return 'Bienvenido a la API de flask'

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

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

if __name__ == '__main__':
    app.run(debug=True)
