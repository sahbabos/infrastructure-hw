from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('new_message')
def handle_new_message(data):
    print(f"Emitting 'new_message' event with data: {data}")  # Confirm this is printed
    socketio.emit('new_message', {'message': data['message']})



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5002, debug=True)
