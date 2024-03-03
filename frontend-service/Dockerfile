# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the service files and tests
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask-SocketIO for testing (if not already in requirements.txt)
RUN pip install flask-socketio

# Set the FLASK_APP environment variable
ENV FLASK_APP=frontend_service.py

# Use an environment variable to determine whether to run tests
ENV RUN_TESTS=false

# Run the tests if the environment variable is true, otherwise run the service
CMD if [ "$RUN_TESTS" = "true" ]; then python -m unittest discover -s tests; else flask run --host=0.0.0.0 --port=5002; fi
