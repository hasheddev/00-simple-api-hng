#!/usr/bin/env python3
'''
    App module for basic api that returns student info
'''

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from os import getenv
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

email = "khidirshola@gmail.com"
github_url = "https://github.com/hasheddev/00-simple-api-hng.git"

@app.route("/")
def hello_world():
    """
        returns basic info about intern
    """
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    response = {"email": email, "current_datetime": current_time, "github_url": github_url}
    return make_response(jsonify(response), 200)

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
