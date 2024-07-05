# Instructional Steps
## Part 1 : Containerization with Docker
### 1.1 Writing Dockerfile to containerize a sample application.
1. Make a file to run the application (app.py)
2. Make a Docker file containing necessary dependencies and configurations (Dockerfile)
3. Make a requirement file containing required Python libraries to be installed with "pip" for application to run (requirements.txt)
### 1.2 Building Docker image
1. Run the following Docker command "docker build -t flask-app ."
2. To check that Docker has successfully generated the image, run "docker image ls"
3. To map the internal Docker port 5000 to local machine's Port 5000, run "docker run -d -p 5000:5000 flask-app"
### 1.3 Test run Docker image
1. Run the following Docker command "docker run flask-app"
2. In Web Browser, enter the local IP address "127.0.0.1:5000"

## Part 2 : Pushing to Docker Hub
### 2.1 & 2.2 Making account & Login in
1. Make account on Docker
2. Run following Docker command "docker login"
3. Enter Docker Hub credentials for username & password from step 1.
### 2.3 Tagging Docker image
1. Run the following Docker command "docker image tag flask-app {namespace}/flask-app, where namespace is replaced with our Docker Hub user ID
2. Verify image tag was successful by running "docker image ls"
### 2.4 Pushing Docker image to Docker Hub
1. Run the following command "docker push {namespace}/flask-app, where namespace is replaced with our Docker Hub user ID
2. To verify successful push, at docker hub web-page, click "Repositories" to view images pushed.

## Part 3 : Setting up Kubernetes
### 3.1 Configuring Kubernetes
1. To verify Kubernetes is running in local environment, run the following command "kubectl get nodes"
### 3.2 Setting up Master & Worker nodes
1. [Steps to set up worker nodes]

## Part 4 : Deploying the Application
### 4.1 Creating Kubernetes deployment YAML file to deploy application
1. Create a new directory (yml)
2. Create a YAML file (deployment.yml) into yml
### 4.2 Configure 3 replicas
1. Run the following command "kubectl scale deployment my-flask-app --replicas=3
2. To verify the newly scaled deployment, run "kubectl get deployments" and "kubectl describe deployment my-flask-app"
### 4.3
### 4.4 Applying the deployment YAML file to Kubernetes cluster
1. Run the following Kubernetes command "kubectl apply -f deployment.yml"
2. Check if deployment is running by running the following code "kubectl get deployments"
