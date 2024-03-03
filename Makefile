.PHONY: minikube-start docker-env build-images apply-manifests open-browser

# Start Minikube
minikube-start:
	minikube start

# Delete the Minikube cluster
cleanup:
	minikube delete

# Build Docker images for your services
build-images:
# Set up the Docker environment to use Minikube's Docker daemon
	eval $$(minikube docker-env) && \
	cd ./receiver-service && docker build -t receiver-service:latest . && \
	cd ../broadcast-service && docker build -t broadcast-service:latest .

# Apply Kubernetes manifests to deploy your services
apply-manifests:
	kubectl apply -f ./kubernetes-manifests/receiver-deployment.yaml && \
	kubectl apply -f ./kubernetes-manifests/receiver-service.yaml && \
	sleep 3 && \
	kubectl apply -f ./kubernetes-manifests/broadcast-deployment.yaml

# Get the URL of the receiver service and open it in the default web browser
open-receiver:
	@echo "Waiting for receiver-service to become available..."
		@until minikube service receiver-service --url; do \
			echo "Waiting for receiver-service..."; \
			sleep 2; \
		done
		@echo "Opening receiver-service in the browser..."
		@minikube service receiver-service --url | xargs open

# Full setup: start Minikube, set up Docker environment, build images, apply manifests, and open the browser
setup: minikube-start docker-env build-images apply-manifests open-receiver
