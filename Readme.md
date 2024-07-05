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

## Part 5 : Persistent Volume Configuration
### 5.1 & 5.2 PVC YAML file
1. Create YAML file for Persistent Volume (PV.yml)
2. Create YAML file for Persistent Volume Claim (PVC.yml)
### 5.3 Mount the PV to container within the Deployment YAML file
1. Modify the Deployment YAML to use the PVC
### 5.4 Log file 
1. Create a Configmap using YAML file (nginx-configmap.yml)
2. Modify the Deployment YAML to mount Configmap in container
3. Run the following commands "kubectl apply -f nginx-configmap.ym", "kubectl apply -f PV.yml", "kubectl apply -f PVC.yml", "kubectl apply -f deployment.yml"
### 5.5 Deleting Deployment and Recreating
1. To delete Deployment, run the following code "kubectl delete deployment {deployment-name}", where deployment-name is defined in deployment.yml file
2. To create a new deployment, run the following command "kubectl apply -f deployment.yml"
### 5.6 Test the container to verify log file is still present in mount path
1. To identify the pod, run "kubectl get pods"
2. To access the pod, run "kubectl exec -it <pod-name> -- /bin/bash, where <pod-name> is to be replaced with the identified pod name in step 1.
3. To verify log file, run "cd /mnt/data" and "ls -l"
4.1. To check the contents of the log file, run "cat nginx-access.log"
4.2. To check errors, run "cat nginx-error.log"

## Part 6 : Expose the Deployment as a Service
### 6.1 Expose deployment as a service of type ClusterIP
1. Run the following command "kubectl expose deployment my-flask-app --type=ClusterIP --port=5000 --target-port=5000" 
2. Another way is to create a YAML file for Service (Service.yml) and then apply it by running "kubectl apply -f Service.yml"
### 6.2 Create a test pod to access service to validate
1. Create YAML file for test pod (test-pod.yml)
2. Apply by running "kubectl apply -f test-pod.yml"
3. Access the test pod by running "kubectl exec -it test-pod -- /bin/bash
4. Test the service by running "curl http://my-flask-app:5000"
5. After testing, cleanup by deleting the test pod. Run "kubectl delete pod test-pod"