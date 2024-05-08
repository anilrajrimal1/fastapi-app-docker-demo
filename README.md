
# Dockerizing Simple Fast-API App

This is a demo project for the demonstration for Dockerizing very Simple python fast-api app. This is created using python (fast-api).

You can also read the requirements.txt file for better understanding of packages and all.



## Steps To Follow

- Clone this repository first 
```bash
git clone https://github.com/anilrajrimal1/fastapi-app-docker-demo.git

```
- Install docker and docker-compose in your system. Read this for Refrence [Documentation](https://docs.docker.com/engine/install/).

- Getinto the cloned directory & Bulid docker image using Dockerfile
```bash
cd fastapi-app-docker-demo
docker build -t <image-name> .
```
- Now run the container
```bash
docker run -d --name <create-container-name> -p 80:80 <image-name>
```
You can add any suitable container name of your choice.
    
