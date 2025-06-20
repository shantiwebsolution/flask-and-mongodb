from flask import Flask, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/api', methods=['GET'])
def api():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500

if __name__ == '__main__':
    app.run(debug=True)
