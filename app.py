import os
import dedupe

from flask import Flask, send_from_directory, make_response, request
from flask import jsonify

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def hello():
    return send_from_directory('static', 'index.html')

@app.route('/run')
def run():
    bank_id = request.args.get('bank_id')
    api_key = request.args.get('api_key')

    if (bank_id is None) or (bank_id == ''):
        return make_response(jsonify({'error': "bank_id can't be blank"}), 401)
    elif (api_key is None) or (api_key == ''):
        return make_response(jsonify({'error': "api_key can't be blank"}), 401)
    else:
        if (api_key == os.environ['MICRO_SERVICE_API_KEY']):
            try:
                dedupe.run(bank_id)
                return make_response(jsonify({'success': 'We received the request'}), 201)

            except Exception as e:
                print(e)
                return make_response(jsonify({'error': 'Please report a bug to team@banker-box.com'}), 500)
        else:
            return make_response(jsonify({'error':'Authentication error: invalid API key'}), 401)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
