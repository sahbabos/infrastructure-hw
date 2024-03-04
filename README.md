# Infrastructure Homework

## Overview

This project is a technical demonstration of a simple Infrastructure  system. the infrastructure for an application with a small set of services to Broadcast and receive "Hello world" messages at random intervals. The messages are viewable from a web browser. The solution is designed to run locally.

The messages are send  in real-time from the broadcast service to the receiver service through a WebSocket connection. Once a message is broadcasted and processed or displayed by the receiver service, it exists only in memory and is not stored anywhere permanently. When the services are restarted these messages will be lost.

## Technology Stack

- **Language:** Python
- **Frameworks:** Flask, Flask-SocketIO, Socket.IO
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)

## Project Structure

- `broadcast-service/`: Contains the Broadcast Service that sends "Hello world" messages at random intervals.
- `receiver-service/`: Contains the Receiver Service that receives messages and displays them on a web page.
- `kubernetes-manifests/`: Contains Kubernetes manifests for deploying the services.
- `Makefile`: Contains commands to automate the setup and teardown of the project.

## Prerequisites

Before running the project, please ensure that you have the following installed:

- **Docker:** [Download Docker](https://www.docker.com/get-started)
- **Minikube:** [Download Minikube](https://minikube.sigs.k8s.io/docs/start/)
- **kubectl:** [Download kubectl](https://kubernetes.io/docs/tasks/tools/)
- **Make:**
  - For Windows: [Download Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm)
  - For macOS: Make is usually pre-installed, but if not, you can install it using [Homebrew](https://brew.sh/): `brew install make`
  - For Linux: Use your package manager to install make, e.g., for Ubuntu/Debian: `sudo apt-get install make`
- **Python 3 (3.9):** [Download Python 3.9](https://www.python.org/downloads/release/python-390/)
- **pip (Python package installer):** pip is usually installed with Python 3.9. If not, you can [download pip](https://pip.pypa.io/en/stable/installation/) or install it using:
  - For Windows/macOS/Linux: `python -m ensurepip --upgrade`

## Installing Python Dependencies - (for Method-3)

Before running the (Method-3), you need to install the required Python packages for both the broadcast and receiver services. Navigate to each service directory and install the dependencies using pip:

```bash
cd broadcast-service
pip install -r requirements.txt

cd ../receiver-service
pip install -r requirements.txt
```
# Running the Project

## Method 1 - With Makefile

Navigate to the directory where you cloned the repository and ensure that the Docker daemon is running.

**Start Minikube and Build Docker Images:**
   ```bash
   make setup
   ```
  This command will start Minikube, build Docker images, deploy the services, and open the Receiver Service in your default web browser.
  
(Note): If you encounter any issues opening the browser, copy the URL from the terminal response and paste it into your web browser to view the webpage..

 **Clean Up:**
   ```bash
   make cleanup
   ```
In the end if you want to cleanup you can run the above command. This will delete the Minikube cluster and remove all associated resources.

## Method 2 - Manual Setup without Makefile

In a case that you are bored and want to have some fun you can take the long route and do all the steps manually.

**Step 1 - Start Minikube:**
```bash
minikube start
   ```
**Step 2 - Set Docker Environment:**

 First, ensure that the Docker daemon is running. The command below will configure your shell to use Minikube's Docker daemon

```bash
eval $(minikube docker-env)
```
**Step 3 - Build Docker Images:**



1. Navigate to receiver-service and build the image:

```bash
cd receiver-service
docker build -t receiver-service:latest .
   ```
2. Navigate to broadcast-service and build the image:
```bash
cd ../broadcast-service
docker build -t broadcast-service:latest .
   ```
**Step 4 - Deploy Services:**
* Navigate to `kubernetes-manifests` dir and apply the manifests. In total we have 3 deployments (Note: receiver needs to be deployed first):
```bash
cd ../kubernetes-manifests
kubectl apply -f receiver-deployment.yaml
kubectl apply -f receiver-service.yaml
kubectl apply -f broadcast-deployment.yaml
   ```
**Step 5 - Access the Receiver Service:**
*  Get the service URL:
```bash
minikube service receiver-service --url
   ```
This should result in a response as:
```
http://127.0.0.1:49306
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```
Open the URL in a web browser to view the received messages.

**Clean Up:**

To cleanup simply delete the cluster
```bash
minikube delete
   ```

## Method 3 -  Manual Setup without using minikube:
you can also run this code without using the minikube or docker. You will be needing 2 terminals.


1. Navigate to receiver-service and run the program:

```bash
cd receiver-service
python receiver-service.py
   ```
   
* After running the receiver service, you will see a URL in the terminal output. Make sure to save this URL. You can use it to access the landing page after running the broadcast service:

```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5002
 * Running on http://192.168.1.173:5002
```

2. Navigate to broadcast-service and run the program:
```bash
cd ../broadcast-service
python broadcast-service.py
```

3. Open a web browser and  enter your url
