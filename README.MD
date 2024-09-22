What is Git?

- Git is a free and opensource version control system, that allows the developers to track changes in files.
  It allows developers to save snapshots of the code, roll back to previous versions, and work on multiple versions simultaneously using branches.

What is Version Control?

- The management of changes to document, computer programs, large websites, and other collection of information.

What is a Repository?

- Project, or the folder where the project is kept.

What is Github?

- GitHub is a cloud-based hosting service for Git repositories. It enables collaboration between multiple developers on the same project, writing the code for the same project without getting conflicts.

Git Commands:

- git init -> Initializes a empty repository
- git clone <url> -> Bring a repository that is hosted somewhere like Github into a folder on your local machine
- git remote add origin <url> -> Add remote repository
- git add <filename> or . -> Track your files and changes in Git.
- git commit -m "Message" -> Save your files in Git
- git push -u origin -> Upload Git commits to a remote repo, like Github
- git pull -> Download changes from remote repo to your local machine, the opposite of push
- git branch -> Display on which branch we are currently
- git branch <branchname> -> Creates a branch
- git checkout <branchname> -> Switches the branch
- git branch -d <branch-name> -> Deletes a branch
- git push origin --delete <branch-name> -> Deletes a branch from the remote repository

What does git add do, and what is the difference between git commit and git push?

- git add stages your changes, making them ready to be committed. git commit saves the changes in your local repository, while git push uploads your local commits to the remote repository on GitHub.

What is the purpose of creating branches in Git?

- Branches allow you to work on new features or fixes in isolation, preventing changes from affecting the main codebase until they are ready to be merged.

What is the difference between git pull and git clone?

- git clone is used to copy a remote repository to your local machine for the first time. git pull is used to fetch and merge changes from the remote repository into your local repository.

What is a PR?

- A pull request (PR) is a way to propose changes you've made in a branch to the main project. It's also where other team members can review, discuss, and approve or reject the changes.

What is the difference between a Pull Request and a merge?

- A Pull Request is a way to propose and review changes before merging them into the main branch. A merge is the actual combination of two branches into one.

- After successfully merging two branches through a PR, you need to pull the changes to the local repo from the remote repo using git pull.

How can someone contribute to your open-source project?

- They can fork the project, make changes in their fork, and submit a pull request to propose their changes.

This is main branch.
This is a change from github.

What is Github Actions?

- GitHub Actions is a tool to automate tasks in your software development lifecycle, such as Continuous Integration (CI) and Continuous Deployment (CD). It allows you to automatically build, test, and deploy your code after every commit.

What is GitHub Actions, and how does it help with CI?

- GitHub Actions automates workflows like testing, building, and deploying code. It helps with Continuous Integration by automatically running tests and other checks every time code is pushed to the repository.

What is Docker?

- Docker is a platform used to develop, ship, and run applications in isolated environments called containers. It allows you to package an application and its dependencies into a single, self-contained unit that can run anywhere.

What is Docker Hub?

- Docker Hub is a cloud-based registry service that allows you to store, distribute, and share Docker images. Think of it as a GitHub for Docker images, where developers can upload images, and others can pull them for use.

What is the primary purpose of Docker, and how does Docker Hub complement Docker?

- Docker is used to create and run containers that bundle applications with their environments. Docker Hub stores and distributes Docker images, enabling easy sharing and deployment of applications.

Docker Image:

- A Docker image is a blueprint for a container, containing everything your application needs to run (code, libraries, environment variables, etc.). It's read-only.

Docker Container:

- A Docker container is a running instance of a Docker image. Containers are lightweight and can be started or stopped quickly. Think of a container as a virtual machine, but far more efficient and isolated.

What is the difference between a Docker image and a Docker container?

- A Docker image is a static blueprint containing everything the application needs to run. A container is a running instance of that image where the application operates.

- Containers are Stateless

Docker Commands:

- docker images -> Shows the locally available images
- docker ps -> Shows the Running Containers
- docker ps -a -> Shows the running and stopped containers
- docker rmi <imageid> -> Deletes a docker image
- docker run <imageid> -> Pulls the image and makes a container
- docker start <containerid> -> Start the container
- docker stop <containerid> -> Stops the container
- docker build -t <imagename> . -> Builds a image
- docker exec -it <containerid> bash -> Goes into the running container directories.

How do you create and run a Dockerfile for a Python Flask application?

- You write a Dockerfile specifying the base image, copy files, install dependencies, and expose a port. Then, you build the image using docker build and run the container using docker run.

Docker Layer:

- Each instruction in a Dockerfile creates a new layer in the Docker image. These layers are cached, meaning that if no changes are detected, Docker will reuse previous layers to speed up builds.

How do Docker layers affect image size and build times?

- Each Dockerfile instruction creates a new layer, and Docker caches these layers. If no changes are made to a layer, Docker will reuse it, reducing the time and size needed for the build.

Docker Registry:

- A Docker registry is a storage and distribution system for Docker images. Docker Hub is the default and public Docker registry. You can also set up private Docker registries.

What is the difference between a Docker registry and Docker Hub?

- A Docker registry is a storage location for Docker images, and Docker Hub is a public registry provided by Docker where you can store, share, and distribute images.

What is Port Mapping and What is it's use?

- Port mapping allows you to make a container’s internal ports accessible on your host machine.

* Run a container with port mapping
* docker run -p 8080:5000 my-flask-app
* In this example, Docker maps the host machine’s port 8080 to the container’s internal port 5000.

Why is port mapping important in Docker, and how is it implemented?

- Port mapping allows communication between your host machine and the running container. It’s implemented using the -p flag, specifying the host port and the container port.

You have a Flask application running inside a Docker container on port 5000, but your organization restricts external access to port 5000. How can you configure Docker to map the container’s internal port 5000 to your host’s port 3000 so that it complies with organizational policies? Provide the Docker run command and explain the importance of port mapping in this scenario.

- docker run -p 3000:5000 my-flask-app

- Port mapping allows you to expose services from a container on a different port than the one used inside the container. In this case, mapping port 5000 to 3000 makes it accessible externally on a port that adheres to the organization’s restrictions.

You run a Docker container without specifying a port mapping, but the application inside the container runs on port 80. Can you access this application from your host machine? Why or why not?

- No, you cannot access the application because no port has been mapped to the host machine. The internal port (80) must be mapped to an external port using -p <host-port>:80.

What is a tag in Docker Hub, and how is it used to identify different versions of a Docker image?

- A tag in Docker Hub is a label that identifies different versions of the same Docker image. Tags are used to differentiate between different builds or versions, such as latest, v1.0, or development. By using tags, you can pull and run specific versions of an image.

If you do not specify a tag when pulling an image from Docker Hub, which version of the image is pulled by default?

- The latest tag is pulled by default if no tag is specified.

Explain the significance of the EXPOSE instruction in a Dockerfile. What role does it play in container networking, and how does it relate to port mapping?

- The EXPOSE instruction in a Dockerfile specifies which port the application inside the container listens to. However, it doesn’t automatically map the container’s port to the host. To make the port accessible outside the container, you still need to use port mapping with the -p flag.

How would you configure a GitHub Actions workflow to run a Docker container, execute tests inside it, and stop the container afterward?

- The workflow would:
  - Build the Docker image.
  - Run the container with the required test commands.
  - Stop the container after tests complete. Example:
    yaml:
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - run: docker build -t my-app .
          - run: docker run my-app pytest tests/
          - run: docker stop $(docker ps -q)


