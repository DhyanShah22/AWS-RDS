from flask import Flask, request, jsonify
from db import create_user, get_users
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    create_user(data['username'], data['email'])
    return jsonify({"message": "User added"}), 201

@app.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
