import os
import time
import random
import socketio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a Socket.IO client
sio = socketio.Client()

# Get the receiver service URL from an environment variable (default to 'http://localhost:5002')
# This is usefull when user trys to use minikube env

RECEIVER_SERVICE_URL = os.getenv(
    'RECEIVER_SERVICE_URL', 'http://localhost:5002')


def connect():
    logging.info("Connected to Receiver Service")


def disconnect():
    logging.info("Disconnected from Receiver Service")


def generate_message():
    # generate a message
    return {"message": "Hello world"}


def send_message(message):
    # send the given message to the sio
    sio.emit('broadcast_message', message)
    logging.info(f"Message sent: {message['message']}")


def get_interval():
    # get a random number between 1-10
    return random.randint(1, 10)


def broadcast_message():
    while True:
        interval = get_interval()
        message = generate_message()
        send_message(message)
        time.sleep(interval)


if __name__ == '__main__':
    try:
        sio.on('connect', connect)
        sio.on('disconnect', disconnect)
        sio.connect(RECEIVER_SERVICE_URL)
        broadcast_message()
    except Exception as e:
        logging.error(f"Failed to connect to Receiver Service: {e}")
    finally:
        sio.disconnect()
