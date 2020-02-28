## Images
Goto https://hub.docker.com/ to find images of different services.

## Commands
### 1. docker run {Image-Name} 
This command runs the docker from an image locally, if not found locally it will pull the image from dockker hub
#### docker run -d {Image-Name}
Runs the image in a detached manner i.e. in the background. 
#### docker run -i {Image-Name}
Runs the container in an interactive way manner
#### docker run -it {Image-Nmae}
Runs the docker with access to terminal ass well as interactive in nature.
#### docker run -p {port-no} {Image-Name}
Allows us to map the docker image to a particular port
#### docker run -v {external-path}:{internal-path} {inamge-name}
Allows us to map data to an external directory.
### 2. docker ps
Gives us all the running docker-images as well as information about them
### 3. docker stop {Docker-Name}
Stops a running docker-image
### 4. docker rm {Image-Name}
Removes the docker images after stopping it
### 5. docker images
Lists all the images present on the local device.
### 6. docker rmi {Image-Name}
Deletes the image-name present on the local device
### 7. docker pull {Image-Name}
Only pulls the image from docker-hub without running it.
### 8. docker exec {docker-container} {command}
Exectues a command on a running docker.
### 9. docker attach {docker-container}
To reattach to a running container (background)
### 10. docker inspect {Image-Name}
Returns data of image/container in a JSON format
