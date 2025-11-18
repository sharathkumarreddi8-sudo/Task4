Sure — here is the exact code you need for Task 4 (Build a REST API with Flask).
It matches your task requirements perfectly: GET, POST, PUT, DELETE, storing users in an in-memory dictionary.

You can directly copy–paste this into app.py and run it.


---

✅ Task 4 — Flask REST API (Final Code)

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id]), 200

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get("id")

    if user_id in users:
        return jsonify({"error": "User ID already exists"}), 400

    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }

    return jsonify({"message": "User created", "user": users[user_id]}), 201

# PUT - Update user details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify({"message": "User updated", "user": users[user_id]}), 200

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)


---
