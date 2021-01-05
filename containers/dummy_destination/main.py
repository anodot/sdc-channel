import json
import os
from flask import Flask, request, jsonify

OUTPUT_DIR = '/app/output'

app = Flask(__name__)


@app.route('/alert', methods=['POST'])
def to_file():
    auth = request.authorization
    if auth.username != 'admin' or auth.password != 'admin':
        return jsonify('Authentication failed'), 401
    with open(os.path.join(OUTPUT_DIR, 'test.json'), 'a+') as f:
        json.dump(request.json, f)
        f.write('\n')
    return ''
