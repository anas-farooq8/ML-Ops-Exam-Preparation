1. What is Docker Compose?
   Docker Compose is a tool that allows you to define and manage multi-container Docker applications. With Docker Compose, you can define multiple services (containers), networks, and volumes in a single YAML file, making it easier to set up and manage complex environments with interconnected services.

Why do we need Docker Compose?

- Multi-Container Applications: When you have multiple containers (e.g., a web server, database, and caching service), Docker Compose lets you define and run them together.
- Consistency: Ensures that all developers use the same environment, defined in a single file.
- Easy Management: Using simple commands (docker-compose up and docker-compose down), you can start or stop all containers specified in the Compose file.
- Automation: Compose simplifies running complex environments without manually starting each container.

2. Docker Compose vs Dockerfile
   Dockerfile: Defines how to build a single Docker image for an application, specifying instructions like FROM, RUN, COPY, and CMD.
   Docker Compose: Manages multiple containers and services. It uses a YAML file (docker-compose.yml) to define how containers interact, connect, and share resources.
   Key Difference: Dockerfile focuses on building an image for one application or service, while Docker Compose is about managing multiple containers.

3. Using Docker Compose for Multiple Application Environments
   To define multiple services, use a docker-compose.yml file. Here’s an example with a simple setup for a web application with a database:

```bash
version: '3.8'
services:
  flask-app:
    build: .
    ports:
      - "8080:8080"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_USER: example
      POSTGRES_PASSWORD: example
      POSTGRES_DB: example_db
```

4. Ensuring Container Order with Docker Compose
   By default, Docker Compose does not wait for containers to be ready. The depends_on directive makes sure that container 1 starts before container 2, but it doesn’t ensure that container 1 is “ready” before container 2 starts. To handle this, use a wait-for-it script or an equivalent health check.

```bash
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    command: ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: example
      POSTGRES_PASSWORD: example
      POSTGRES_DB: example_db
```

5. CMD vs ENTRYPOINT
   CMD: Provides default arguments for a container. It can be overridden by passing arguments in the docker run command.
   ENTRYPOINT: Sets a fixed command that always runs in the container. The arguments can be appended but not replaced.

# ENTRYPOINT example

ENTRYPOINT ["echo"]

# CMD example

CMD ["Hello, World!"]

6. Managing Volumes and Networks in Docker Compose
   Volumes allow data to persist outside of containers, so it’s not lost when the container stops.
   Networks provide isolated communication channels for containers to talk to each other.

```bash
version: '3.8'
services:
  web:
    image: nginx
    volumes:
      - web_data:/usr/share/nginx/html
    networks:
      - my_network

  db:
    image: postgres:13
    networks:
      - my_network

volumes:
  web_data:

networks:
  my_network:

```

7. Circumstances for Losing Data in a Container and Solutions
   Data in a container can be lost if:

The container stops or is removed (since containers are stateless by default).
A new container is created without mounting the same volume.
Solution: Use Docker Volumes
Using Docker volumes allows data persistence outside of the container, so it’s retained even if the container is removed.

```bash
services:
  db:
    image: postgres:13
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

8. Virtualization vs Containerization
   Virtualization involves running multiple operating systems on a single physical machine, with each virtual machine (VM) having its own OS and resources. Containerization packages applications with their dependencies in isolated environments, sharing the host OS kernel for efficiency.

Virtualization:
Hardware -> Hypervisor -> VMs (each with separate OS)

Containerization:
Hardware -> OS -> Containers (share OS kernel)

Jenkins

1. Webhooks vs Polling
   Webhooks
   Definition: Webhooks are a way for one application to send real-time data to another when certain events occur. For Jenkins, a webhook in GitHub can trigger a Jenkins pipeline automatically whenever there’s a code change, such as a push to a branch.
   Use Case: Webhooks are preferred over polling when you want Jenkins to respond immediately to changes in a repository without the need to repeatedly check for updates.
   Polling
   Definition: Polling is a method where Jenkins periodically checks the source repository for changes. If changes are detected, it triggers the pipeline.
   Use Case: Polling is useful when a webhook is not set up or supported. However, it can be less efficient since it requires Jenkins to continuously check for changes.
   When to Use Which:
   Webhooks are generally preferable for real-time CI/CD pipelines as they reduce the load on Jenkins and GitHub.
   Polling can be a fallback when webhooks cannot be set up due to permissions or firewall restrictions.

2. Docker Integration with Jenkins
   Jenkins can use Docker to build, test, and deploy applications within containers, ensuring that the build environment remains consistent. You can define Docker commands within Jenkins pipelines to:

Build Docker images for your application.
Run Docker containers to execute tests or deploy applications.
Push Docker images to registries like Docker Hub or GitHub Packages.

3. Multibranch Pipeline in Jenkins
   Definition: A Multibranch Pipeline job in Jenkins automatically discovers, manages, and executes branches in a repository that contain a Jenkinsfile. Each branch can have its own pipeline configuration.
   Benefits: This setup is particularly useful in CI/CD workflows where different branches need specific configurations or processes.
   Example: In a project with dev and main branches, a Multibranch Pipeline can run different pipelines (e.g., build and test for dev, build, test, and deploy for main).

4. Using Parameters in Jenkins
   Parameters allow you to make Jenkins pipelines flexible by accepting inputs during the build process. Types of parameters include:

String: For text input.
Choice: Allows selecting from a set of options.
Boolean: For true/false choices.

5. Ngrok and its Use
   Ngrok is a tool that creates secure tunnels to expose a local web server to the internet. In Jenkins, ngrok can be used to:

Expose Jenkins running on a local machine to the internet, which is especially useful when setting up webhooks from GitHub.
Enable external access to Jenkins, which is not typically available when hosted locally.

- Explain how you would expose a local Jenkins instance to the internet.

Answer: Using ngrok, you can expose a local Jenkins server to the internet by creating a secure tunnel. This is helpful for setting up webhooks from GitHub to Jenkins, allowing it to receive change notifications even when running locally.

- Why are parameters useful in Jenkins pipelines? Provide an example.

Answer: Parameters allow flexibility in pipelines by letting users specify inputs at runtime, like environment and build version. For example, in a deployment pipeline, parameters like ENVIRONMENT (dev/prod) and BUILD_VERSION (1.0.0) can adjust the deployment behavior.

- What is the purpose of withCredentials in Jenkins when pushing a Docker image to Docker Hub?

Answer: withCredentials securely accesses credentials stored in Jenkins (e.g., Docker Hub credentials) during the pipeline. It allows authentication to Docker Hub without hardcoding sensitive information in the pipeline code.

Case Study
Scenario:
You need to set up a CI/CD pipeline where every push to a GitHub repository triggers a Jenkins job that builds a Docker image and deploys it to a staging environment. However, the GitHub repository does not support webhooks. Describe how you would implement this using polling and Docker integration.
Solution:

1. Configure Jenkins to Poll the GitHub Repository:
   o Job Configuration:
    Navigate to the Jenkins job configuration.
    Under Build Triggers, enable Poll SCM.
    Set the polling schedule, e.g., H/5 \* \* \* \* (every 5 minutes).
2. Define Jenkins Pipeline to Build and Deploy Docker Image:

```bash
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourrepo/app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t yourdockerhub/app:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push yourdockerhub/app:latest'
                }
            }
        }
        stage('Deploy to Staging') {
            steps {
                sh 'docker run -d -p 80:80 yourdockerhub/app:latest'
            }
        }
    }
}
```

Case Study
Scenario:
You are tasked with setting up a Jenkins pipeline for deploying a web application to multiple environments: development, staging, and production. Each environment requires different configuration parameters such as database credentials, API endpoints, and environment-specific settings. As part of the pipeline, you need to prompt the user to input these parameters dynamically during the build process. How would you utilize Jenkins to dynamically configure the deployment process for each environment? Provide a step-by-step explanation of how you would achieve this.
Answer:

```bash
pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['development', 'staging', 'production'], description: 'Select deployment environment')
        string(name: 'DB_CREDENTIALS', defaultValue: '', description: 'Database Credentials')
        string(name: 'API_ENDPOINT', defaultValue: '', description: 'API Endpoint')
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourrepo/app.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Build steps
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Test steps
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (params.ENVIRONMENT == 'development') {
                        // Deploy to development
                    } else if (params.ENVIRONMENT == 'staging') {
                        // Deploy to staging
                    } else if (params.ENVIRONMENT == 'production') {
                        // Deploy to production
                    }
                }
            }
        }
    }
}
```

Jenkins Master-Slave Architecture
In Jenkins, a master-slave architecture (also known as controller-agent) is used to distribute the workload across multiple machines, allowing efficient handling of complex and large-scale projects. Here’s a breakdown of the components and their roles:

- Master (Controller)
  The master (or controller) is the central Jenkins server.
  It is responsible for:
  Managing Jenkins configuration and user permissions.
  Scheduling jobs and assigning them to appropriate slaves.
  Executing jobs when required (although ideally, most jobs should run on slaves).
  Monitoring agents (slaves) and communicating with them.
  Processing results from jobs run on slaves and displaying them in the UI.
- Slave (Agent)
  Slaves (or agents) are machines configured to perform Jenkins jobs as directed by the master.
  They can run on different operating systems and are used to:
  Execute jobs assigned by the master, allowing parallel builds and tests.
  Run specialized jobs, such as tests that require specific hardware, software, or configurations.
  Offload the workload from the master, making the Jenkins environment scalable and distributed.
  A Jenkins environment can have multiple slaves, each with different configurations to handle specific tasks.
  Benefits of Master-Slave Architecture
  Scalability: Multiple slaves can handle a large volume of builds and tests simultaneously.
  Resource Optimization: Jobs can run on specific slaves with the necessary resources or configurations.
  Load Balancing: Distributes the processing load, improving the master server’s performance and response time.

Poll SCM for Changes : Configure job > Build Triggers > Poll SCM > Define cron syntax for interval

Kubernetes
Kubernetes Architecture
Overview
Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It abstracts the underlying infrastructure, providing a robust platform for running applications in production environments.
Core Components
Master Node Components:
• API Server: Exposes the Kubernetes API, acting as the front-end for the control plane.
• etcd: A distributed key-value store that stores all cluster data.
• Controller Manager: Runs controllers that regulate the state of the cluster.
• Scheduler: Assigns pods to nodes based on resource availability and policies.
Worker Node Components:
• kubelet: An agent that ensures containers are running in pods.
• kube-proxy: Manages network routing to pods.
• Container Runtime: Software (e.g., Docker, containerd) that runs containers.
Detailed Explanation
Kubernetes Architecture:
• Master Node:
o API Server: Central point of interaction for managing the cluster.
o etcd: Ensures cluster state is stored reliably.
o Controller Manager: Handles various controllers like Node Controller, Replication Controller.
o Scheduler: Determines which node should run a pod based on resource needs.
• Worker Node:
o kubelet: Communicates with the API server, manages pod lifecycle.
o kube-proxy: Facilitates networking by managing IP tables.
o Container Runtime: Executes container images, e.g., Docker.
Ingress vs. NodePort:
• Ingress:
o Manages external HTTP/HTTPS access to services.
o Provides features like load balancing, SSL termination, and name-based virtual hosting.
o Requires an Ingress Controller.
• NodePort:
o Exposes a service on a static port on each node’s IP.
o Accessible externally via NodeIP:NodePort.
o Simpler but less flexible compared to Ingress.

Pods: The smallest deployable units in Kubernetes, encapsulating one or more containers with shared storage/networking.

ReplicaSets: Ensures that a specified number of pod replicas are running at all times, allowing for scaling and availability.

Deployments: A higher-level abstraction that manages ReplicaSets and provides declarative updates to applications.

Services: An abstraction that defines a logical set of pods and a policy by which to access them. Services enable stable networking for pods.

Ingress: Manages external access to services, typically HTTP, and can provide load balancing and SSL termination.

YAML Files in Kubernetes:
YAML files define Kubernetes resources like pods, services, deployments, and ingress. They specify the desired state, configurations, and relationships between resources.
Pros and Advantages of Kubernetes:
• Scalability: Automatically scales applications based on demand.
• Self-Healing: Restarts failed containers, replaces and reschedules pods.
• Declarative Configuration: Manage infrastructure as code for consistency and versioning.
• Service Discovery and Load Balancing: Automatically assigns IPs and balances traffic.
• Portability: Runs on various environments (on-premises, cloud).
Sample Questions
Q11. (3 Marks) Explain the importance of Ingress in Kubernetes by using a diagram.
Answer:
Ingress manages external access to services within a Kubernetes cluster, typically HTTP/HTTPS traffic. It provides advanced routing capabilities, SSL termination, and load balancing, enabling scalable and secure access to applications.
(Note: Insert a diagram showing Ingress routing traffic to multiple services.)
Q12. (4 Marks) Briefly explain how Kubernetes maintains the status of the cluster according to the configuration file. Mention different scenarios and how they are handled by Kubernetes.
Answer:
Kubernetes continuously monitors the actual state of the cluster against the desired state defined in configuration files. If discrepancies arise, Kubernetes takes corrective actions to reconcile them.
Scenarios:

1. Pod Failure:
   o Desired State: 3 replicas running.
   o Actual State: 2 replicas running.
   o Action: Kubernetes schedules a new pod to meet the desired state.
2. Node Failure:
   o Desired State: Pods distributed across nodes.
   o Actual State: Nodes unavailable.
   o Action: Kubernetes reschedules pods on healthy nodes.
3. Scaling:
   o Desired State: Increase replicas to 5.
   o Actual State: Currently 3 replicas.
   o Action: Kubernetes creates 2 additional pods.

Kubernetes Architecture Overview
Kubernetes is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications. It provides a robust framework for managing applications in a microservices architecture, enabling applications to run in a highly available and scalable manner.

Key Components of Kubernetes Architecture
Master Node: The control plane of a Kubernetes cluster, responsible for managing the state of the cluster. It consists of several components:

API Server: The interface for all interactions with the Kubernetes cluster. It processes REST requests and updates the cluster state.
Controller Manager: Maintains the desired state of the cluster. It manages controllers that handle the routine tasks in the cluster, such as replication and node management.
Scheduler: Assigns newly created pods to nodes based on resource availability and constraints.
etcd: A distributed key-value store that holds the configuration data and state of the Kubernetes cluster.
Worker Node: Where the applications (containers) are actually run. Each worker node has:

Kubelet: An agent that runs on each node, responsible for managing the containers on the node and communicating with the API server.
Kube Proxy: Maintains network rules for pod communication and load balancing.
Container Runtime: Software responsible for running containers (e.g., Docker, containerd).
Pods: The smallest deployable units in Kubernetes, encapsulating one or more containers with shared storage/networking.

ReplicaSets: Ensures that a specified number of pod replicas are running at all times, allowing for scaling and availability.

Deployments: A higher-level abstraction that manages ReplicaSets and provides declarative updates to applications.

Services: An abstraction that defines a logical set of pods and a policy by which to access them. Services enable stable networking for pods.

Ingress: Manages external access to services, typically HTTP, and can provide load balancing and SSL termination.

Volumes: Persistent storage abstractions that allow data to persist beyond the lifecycle of a pod.

Kubernetes Configuration Files
Kubernetes uses YAML or JSON files to define the desired state of the system. Here’s a breakdown of different parts of the Kubernetes configuration files:

apiVersion: Defines the version of the Kubernetes API to use for the object (e.g., apps/v1 for deployments).

kind: Specifies the type of Kubernetes object (e.g., Deployment, Service, Pod).

metadata: Provides data that helps uniquely identify the object, such as name, namespace, and labels.

spec: The specification of the desired behavior of the object. It contains various fields depending on the kind of object being defined:

For a Deployment, it includes replicas, selector, and template.
For a Service, it includes selector, ports, and type.
status: This is automatically populated by Kubernetes and reflects the current state of the object.

Kubernetes Architecture Overview
Kubernetes is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications. It provides a robust framework for managing applications in a microservices architecture, enabling applications to run in a highly available and scalable manner.

Key Components of Kubernetes Architecture
Master Node: The control plane of a Kubernetes cluster, responsible for managing the state of the cluster. It consists of several components:

API Server: The interface for all interactions with the Kubernetes cluster. It processes REST requests and updates the cluster state.
Controller Manager: Maintains the desired state of the cluster. It manages controllers that handle the routine tasks in the cluster, such as replication and node management.
Scheduler: Assigns newly created pods to nodes based on resource availability and constraints.
etcd: A distributed key-value store that holds the configuration data and state of the Kubernetes cluster.
Worker Node: Where the applications (containers) are actually run. Each worker node has:

Kubelet: An agent that runs on each node, responsible for managing the containers on the node and communicating with the API server.
Kube Proxy: Maintains network rules for pod communication and load balancing.
Container Runtime: Software responsible for running containers (e.g., Docker, containerd).
Pods: The smallest deployable units in Kubernetes, encapsulating one or more containers with shared storage/networking.

ReplicaSets: Ensures that a specified number of pod replicas are running at all times, allowing for scaling and availability.

Deployments: A higher-level abstraction that manages ReplicaSets and provides declarative updates to applications.

Services: An abstraction that defines a logical set of pods and a policy by which to access them. Services enable stable networking for pods.

Ingress: Manages external access to services, typically HTTP, and can provide load balancing and SSL termination.

Volumes: Persistent storage abstractions that allow data to persist beyond the lifecycle of a pod.

Kubernetes Configuration Files
Kubernetes uses YAML or JSON files to define the desired state of the system. Here’s a breakdown of different parts of the Kubernetes configuration files:

apiVersion: Defines the version of the Kubernetes API to use for the object (e.g., apps/v1 for deployments).

kind: Specifies the type of Kubernetes object (e.g., Deployment, Service, Pod).

metadata: Provides data that helps uniquely identify the object, such as name, namespace, and labels.

spec: The specification of the desired behavior of the object. It contains various fields depending on the kind of object being defined:

For a Deployment, it includes replicas, selector, and template.
For a Service, it includes selector, ports, and type.
status: This is automatically populated by Kubernetes and reflects the current state of the object.

Multiple Pods Upping in Kubernetes
To scale applications in Kubernetes, you can define the number of replicas in a deployment configuration. The spec.replicas field in the deployment YAML file specifies how many pod instances should be running. For example:

yaml
Copy code
spec:
replicas: 3 # This will create 3 pods
How Kubernetes Maintains the Cluster State
Kubernetes continuously monitors the state of the cluster to ensure that it matches the desired state defined in the configuration files. This is achieved through a control loop mechanism where the control plane continuously compares the desired state (as defined in YAML files) to the actual state (as reflected in the cluster). If a discrepancy is detected, Kubernetes takes corrective action.

Scenarios and How Kubernetes Handles Them
Node Failure: If a node goes down, Kubernetes will detect the failure through the health checks performed by the kubelet. It will automatically reschedule the pods that were running on the failed node to other healthy nodes.

Pod Crash: If a pod crashes, the kubelet will restart it automatically. This is part of the self-healing capability of Kubernetes.

Scaling Up/Down: When you update a deployment to change the number of replicas, the Kubernetes scheduler will create or terminate pods as necessary to meet the desired count.

Resource Constraints: If a pod consumes too many resources and is evicted from a node due to insufficient resources, Kubernetes will attempt to schedule the pod on a different node with sufficient resources.

Importance of Ingress
Ingress is an API object that manages external access to the services in a Kubernetes cluster, typically HTTP. It provides several key benefits:

Routing: Ingress allows you to define rules for routing traffic to different services based on URL paths or hostnames.
SSL Termination: Ingress can handle SSL/TLS termination, allowing you to manage certificates centrally.
Load Balancing: It can provide load balancing for incoming requests, distributing traffic across multiple pods.

StatefulSet in Kubernetes
A StatefulSet is a Kubernetes controller that manages the deployment and scaling of a set of pods, and it provides guarantees about the ordering and uniqueness of these pods. StatefulSets are particularly useful for applications that require persistent storage and stable network identities, such as databases, key-value stores, and other applications that maintain state.

Key Features of StatefulSets:
Stable Network Identity: Each pod in a StatefulSet has a unique, stable network identifier that does not change when the pod is rescheduled. The pods are addressed by their hostname, which is derived from the StatefulSet's name and the ordinal number of the pod (e.g., web-0, web-1, etc.).

Persistent Storage: StatefulSets can use persistent storage volumes associated with each pod. When a pod is created, it can dynamically provision a PersistentVolumeClaim (PVC) that is tied to the pod's identity.

Ordered Deployment and Scaling: StatefulSets ensure that pods are started, stopped, and scaled in a defined order. For example, when scaling up, a StatefulSet creates new pods in order from 0 to N-1, and when scaling down, it removes them in reverse order.

Rolling Updates: StatefulSets support rolling updates, allowing for controlled updates to pods without downtime.

Creating a StatefulSet for a Database
When using StatefulSets to create pods for a database, the typical approach involves defining a StatefulSet resource that specifies the database configuration, including the persistent volume claims for data storage. Here's an example of how you might define a StatefulSet for a MySQL database:

```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```

NodePort and Ingress in Kubernetes
NodePort and Ingress are two methods to expose services in Kubernetes.

NodePort
A NodePort is a way to expose a service on a static port on each node's IP address. When you create a service of type NodePort, Kubernetes allocates a port from a range (default is 30000-32767) and routes traffic from that port on the node to the service.
This is useful for direct access to your application from outside the cluster but may not be ideal for production environments, as it exposes all nodes and requires manual load balancing.

```bash
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30001
  selector:
    app: my-app

```

Ingress
Ingress is a powerful way to manage external access to services in a Kubernetes cluster, providing HTTP and HTTPS routing to services based on host and path.
It allows you to define rules for routing requests to different services and can handle SSL termination and load balancing.
Ingress controllers (such as Nginx Ingress Controller or Traefik) are required to manage Ingress resources.
Example of Ingress Resource:

```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80

```

Summary
StatefulSets are used to manage stateful applications, ensuring stable identities and persistent storage.
NodePort allows access to services via static ports on each node but has limitations for production.
Ingress provides a flexible way to route traffic to services and is suitable for handling HTTP/S requests in a more controlled manner.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Steps](#setup-steps)
- [Accessing PHPMyAdmin](#accessing-phpmyadmin)
- [Flask Application Setup](#flask-application-setup)
- [Conclusion](#conclusion)

## Prerequisites

- **Minikube**: Ensure that you have Minikube installed and running.
- **Kubectl**: You should have kubectl installed to interact with your Kubernetes cluster.
- **Docker**: Docker must be installed for image handling.

## Setup Steps

### Step 1: Starting Minikube

```bash
minikube start
```

### Step 2: Pulling Docker Images in Minikube

Since Minikube uses a local Docker registry, we’ll need to pull the images for MySQL and PHPMyAdmin.

```bash
minikube ssh docker pull mysql
minikube ssh docker pull phpmyadmin
```

### Viewing Docker Images in Minikube

When using Minikube, Docker images are pulled into Minikube's internal Docker environment rather than your local Docker daemon.

```bash
minikube ssh docker images
```

### Step 3: Creating a Secret for MySQL Credentials

Create a Kubernetes Secret to store the MySQL root password securely. This secret will be referenced by the MySQL deployment for authentication.

```bash
kubectl apply -f mysql-secret.yaml
kubectl get secrets
```

### Step 4: Creating the MySQL Deployment

Define a MySQL deployment configuration where the secret created for the root password is referenced, along with environment variables for the database name, username, and password.

```bash
kubectl apply -f mysql-deployment.yaml
kubectl get deployment
```

### Step 5: Defining the MySQL Service

```bash
kubectl apply -f mysql-service.yaml
kubectl get service
```

### Step 6: Creating the PHPMyAdmin Deployment

```bash
kubectl apply -f phpmyadmin-deployment.yaml
kubectl get deployment
```

### Step 7: Creating a Service for PHPMyAdmin

```bash
kubectl apply -f phpmyadmin-service.yaml
kubectl get service
```

### Step 8: Accessing PHPMyAdmin

1. Run the following command to get the PHPMyAdmin service URL:

```bash
minikube service phpmyadmin-service --url
```

2. Log in to PHPMyAdmin using:

```bash
Username: testuser (the MySQL user)
Password: testpass (the MySQL user password)
```

## Flask Application Setup

After testing PHPMyAdmin, we created a Flask application to interact with the MySQL database. The following steps were taken:

### Step 1: Creating the Flask Application

Developed a simple Flask application (`app.py`) to fetch data from the MySQL database.

### Step 2: Creating the Dockerfile

A Dockerfile was created to containerize the Flask application:

```dockerfile
FROM python:3.8-slim

WORKDIR /app

# Install Flask and MySQL connector
RUN pip install flask mysql-connector-python

# Copy the app code and templates folder
COPY app.py .
COPY templates/ templates/

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose port 5000 for the app
EXPOSE 5000

# Start the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

### Step 3: Building the Docker Image

The Docker image was built using the following command:

```bash
docker build -t mysql-data-loader .
```

### Step 4: Loading the Image into Minikube

The image was loaded into Minikube with the following command:

```bash
minikube image load mysql-data-loader
```

### Step 5: Creating the Flask Application Deployment

A deployment for the Flask application was created in Kubernetes.

```bash
kubectl apply -f flask-deployment.yaml
kubectl get deployment
```

### Step 6: Creating an External Service for the Flask Application

An external service was created to expose the Flask application.

```bash
kubectl apply -f flask-service.yaml
kubectl get service
```

### Step 7: Testing the Flask Application

Tested the Flask application, which successfully fetched data from the MySQL database.

## Conclusion

You now have a fully functional MySQL setup running on Kubernetes, along with PHPMyAdmin for easy database management and a Flask application for data interaction. You can customize this setup further by adjusting the configurations as needed.
