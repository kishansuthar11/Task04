from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    if not request.is_json:
        return jsonify({"error": "Invalid input, expected JSON"}), 400
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"message": "User created", "user_id": user_id}), 201

@app.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    if not request.is_json:
        return jsonify({"error": "Invalid input, expected JSON"}), 400
    data = request.get_json()
    users[user_id] = data
    return jsonify({"message": "User updated"}), 200

@app.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
