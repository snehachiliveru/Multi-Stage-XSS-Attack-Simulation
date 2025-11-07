# simple Flask logger: receives JSON POSTs at /log and appends to logs/logs.txt
from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "logs.txt")
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/")
def index():
    return "Safe logger running. POST JSON to /log"

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "send JSON body"}), 400
    entry = {
        "time": datetime.utcnow().isoformat() + "Z",
        "data": data
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(str(entry) + "\n")
    return jsonify({"status": "ok"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
