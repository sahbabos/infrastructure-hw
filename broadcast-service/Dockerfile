# Base stage for both service and tests
FROM python:3.8-slim as base

# Copy the entire project
COPY . /usr/src/app

# Install dependencies
WORKDIR /usr/src/app/broadcast-service
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory back to the project root
WORKDIR /usr/src/app

# Service stage
FROM base as service

WORKDIR /usr/src/app/broadcast-service
CMD ["python", "broadcast_service.py"]

# Test stage
FROM base as test

WORKDIR /usr/src/app/tests/broadcast
CMD ["python", "-m", "unittest", "discover"]
