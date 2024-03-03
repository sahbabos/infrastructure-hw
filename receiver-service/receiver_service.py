from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


def log_message(data):
    print(f"Received broadcast message: {data['message']}")


def emit_message(data):
    socketio.emit('new_message', {'message': data['message']})


@socketio.on('broadcast_message')
def handle_broadcast_message(data):
    log_message(data)
    emit_message(data)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5002,
                 debug=True, allow_unsafe_werkzeug=True)
