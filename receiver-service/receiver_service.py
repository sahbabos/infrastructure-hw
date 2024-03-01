from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message', None)
    if message is None:
        logging.error("Invalid message format")
        return jsonify({'status': 'error', 'message': 'Invalid message format'}), 400
    else:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Received message: {message} at {timestamp}")
        return jsonify({'status': 'success', 'message': 'Message received', 'received_message': message, 'timestamp': timestamp}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
