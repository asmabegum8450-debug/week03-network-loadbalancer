import os
from flask import Flask, jsonify

app = Flask(__name__)

SERVER_ID = os.getenv("SERVER_ID", "unknown")

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from the private subnet!",
        "server": SERVER_ID
    })

@app.route("/healthz")
def health():
    return jsonify({
        "status": "healthy",
        "server": SERVER_ID
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
