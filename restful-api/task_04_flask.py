from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=['GET'])
def get():
    
    return jsonify(users)

@app.route("/status", methods=['GET'])
def status():
    return "OK"

@app.route("/users/<username>", methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User Error"}), 404
@app.route("/add_user", methods=['POST'])

if __name__ == "__main__": app.run()