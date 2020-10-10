import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/gdp', methods=["GET"])
def index():
    return json.dumps([
        {"country": "USA", "value": 20.5},
        {"country": "China", "value": 13.4},
        {"country": "Germany", "value": 4.0},
        {"country": "Japan", "value": 4.9},
        {"country": "France", "value": 2.8}
    ])


app.run()
