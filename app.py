from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_unixtime():
    unix_time = int(time.time())
    return jsonify({'unixtime': unix_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
