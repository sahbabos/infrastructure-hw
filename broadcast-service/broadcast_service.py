import time
import random
import requests
import logging
import signal
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Flag to control the broadcasting loop
running = True

def broadcast_message():
    url = "http://localhost:5000/receive"  # URL of the Receiver Service
    while running:
        interval = random.randint(1, 10)
        message = {"message": "Hello world"}
        try:
            response = requests.post(url, json=message)
            if response.status_code == 200:
                logging.info(f"Message sent: {message['message']}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send message: {e}")
        time.sleep(interval)

def signal_handler(sig, frame):
    global running
    running = False
    logging.info("Shutting down broadcast service...")

if __name__ == "__main__":
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    broadcast_message()
