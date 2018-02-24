# Docker

## Docker Registry

```
docker login -u docker -p (pw) -e docker@mycompany.com docker.mycompany.com

# Edit /etc/default/docker:
DOCKER_OPTS="--insecure-registry docker.mycompany.com"

# See docker group
cat /etc/group | grep docker
```

## Common commands

```
docker login -u docker -p (pw) -e docker@mycompany.com docker.mycompany.com

# Edit /etc/default/docker:
DOCKER_OPTS="--insecure-registry docker.mycompany.com"

# To pull an image from the Docker registry:
docker pull docker.mycompany.com/build_envs/imageName:imageName
docker pull docker.mycompany.com/build_envs/imageName         # pull only imageName:latest
docker pull docker.mycompany.com/build_envs/imageName:3.0
docker pull docker.mycompany.com/build_envs/imageName:3.0.0

# Remove all non-running ("exited") containers	
docker rm $(docker ps -q -f status=exited)

# Remove all dangling images
docker rmi $(docker images -q -f dangling=true)

# Other options/filters
# -q (quiet)
# -f (filter)
# -f, --filter value    Filter output based on conditions provided (default [])
#                       - dangling=(true|false)
#                       - label=<key> or label=<key>=<value>
#                       - before=(<image-name>[:tag]|<image-id>|<image@digest>)
#                       - since=(<image-name>[:tag]|<image-id>|<image@digest>)
#                       - reference=(pattern of an image reference)

# Copy
docker cp <containerId>:/path/to/file /host/path/to/file
```

## Docker - attach to a running container
See also [link](http://askubuntu.com/questions/505506/docker-how-to-get-bash-ssh-inside-runned-container-run-d).

```
# by ID
sudo docker exec -i -t 665b4a1e17b6 bash
# or by Name
sudo docker exec -i -t loving_heisenberg bash
root@665b4a1e17b6:/#
```

## Docker - start a container of an image

```
docker run -t -i mycompany/imageName:v1.0.0b2 /bin/bash
```


## Build and image and upload to server manually

```
# Build image
$ docker build -t mycompany/imageName:v1.0.0b2 .

# Delete image
$ docker rmi <IMAGE_ID>

# Get the image to the server:
$ docker save mycompany/imageName:v1.0.0b2 | bzip2 | pv | ssh your_name@your_server 'bunzip > imageName.img'

# Start the image
$ docker run --mac-address=02:20:12:30:e4:cg -v /opt/gurobi:/opt/gurobi:ro docker.mycompany.com/build_envs/imageName:3.5 solve -h 
or
$ docker run --mac-address=`ifconfig eth0 | grep HWaddr | sed 's/.*HWaddr \(..:..:..:..:..:..\).*/\1/'` -v /opt/gurobi:/opt/gurobi:ro docker.mycompany.com/build_envs/imageName:3.5 solve -h

# On the server (your_name@your_server), import the image into the server's docker image list
$ docker load -i imageName.img

# on your_name@your_server

# List all containers
$ docker ps -a

# Rename existing container
$ docker rename old_name new_name

# Create container  
$ docker create --name imageName -v /opt/gurobi:/opt/gurobi:ro -v /opt/gurobi603:/opt/gurobi603:ro -v /etc/localtime:/etc/localtime:ro -e LD_LIBRARY_PATH=/opt/gurobi603/linux64/lib --net=host --restart=always mycompany/imageName:v1.0.0b3

# Delete container
$ docker rm <CONTAINER_ID>
```

## Docker issue

Error starting containers in 1.7.1 - could not find bridge docker0: no such network interface #14738
https://github.com/docker/docker/issues/14738

Solution:

```
sudo service docker restart
```
