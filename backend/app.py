"""
Tiny Flask API for the CI/CD teaching demo.

Endpoints:
    GET /api/health        -> {"status": "ok"}
    GET /api/greet/<name>  -> {"message": "Hello, <name>!"}
    POST /api/add          -> {"result": a + b}   body: {"a": 1, "b": 2}

Kept deliberately small so students can focus on the CI/CD pipeline
around it, not the app itself.
"""
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # allow the React dev server to call this API


@app.get("/api/health")

def health():
    return jsonify(status="ok")


@app.get("/api/greet/<name>")
def greet(name):
    if not name.strip():
        return jsonify(error="name must not be empty"), 400
    return jsonify(message=f"Hello, {name}!")


@app.post("/api/add")
def add():
    data = request.get_json(silent=True) or {}
    if "a" not in data or "b" not in data:
        return jsonify(error="body must include 'a' and 'b'"), 400
    try:
        a = float(data["a"])
        b = float(data["b"])
    except (TypeError, ValueError):
        return jsonify(error="'a' and 'b' must be numbers"), 400
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
