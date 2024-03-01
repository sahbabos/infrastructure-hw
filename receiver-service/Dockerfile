# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the service files and tests
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Use an environment variable to determine whether to run tests
ENV RUN_TESTS=false

# Run the tests if the environment variable is true, otherwise run the service
CMD if [ "$RUN_TESTS" = "true" ]; then python -m unittest discover -s tests; else python receiver_service.py; fi
