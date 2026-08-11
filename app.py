from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "Hello from Flask",
        "status": "running"
    })

@app.get("/users/<int:user_id>")
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": f"User {user_id}"
    })

if __name__ == "__main__":
    app.run(debug=True)
