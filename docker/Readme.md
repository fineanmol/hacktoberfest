
#  Docker Cmd

> **login** : docker login

> **Index** : https://app.eraser.io/workspace/yTPql82lXyOpbyX63Xgn

##  Links:

- **All docker images are available at** : [hub.docker.com](hub.docker.com)

## Attribute:

- **-it**: interactive, connect the main cmd to container cmd , and don't disconnect

- **-t**: tag (name)

  

##  Main Line cmd:

- **to make image/container** : install any image that will automatically make a container. **Cmd** : docker run -it ubuntu
- **to go inside any container** : docker start -i thanos(container_name)
- **to go inside if container is already running**: docker exec -it thanos bash
- **to run any cmd inside container** : docker exec *container_name* ls. **eg:** docker exec pendatic_mendel ls
- **to see images** : docker image ls

- **Port mapping** : docker run -it p 1025:1025 container_name

- **Port mapping with evn set** : docker run -it -p 1025:1025(my_machine_Port:docker_port) -e key=value -e key=value continer_name. **eg** docker run -it -e PORT=4000 -p 4000:4000 first-nodejs

- **to build dockerfile** : docker build -t -image name you want to give- . (path)


##  Container cmd:

- **to see active** : docker container ls

- **to see all active** : docker container ls -a

- **to start container** : docker start -container name- , eg: docker start pedantic_mendel

- **to stop container** : docker stop pendatic_mendel

  

##  Dockerfile

save the file with name : "dockerfile" where package.json is present

    FROM ubuntu
    
    RUN apt-get update
    
    RUN apt-get install -y curl
    
    RUN apt-get upgrade -y
    
    RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
    
    RUN apt-get upgrade -y
    
    RUN apt-get install -y nodejs
    
      
    
    WORKDIR /usr/app
    
    COPY package.json package.json
    
    COPY package-lock.json package-lock.json
    
    COPY index.js index.js
    
      
    
    RUN npm install
    
      
    

Now run : docker build -t first-nodejs .

  

## Layer Caching

>inside dockerfile if any line execute every time when building dockerfile then docker cache it and start building again from line where changes happened.

1. **Layered Architecture**: Each command in a Dockerfile (like `COPY`, `RUN`, etc.) creates a new layer on top of the previous one. These layers build up the final image.
   
2. **Cache Reuse**: Docker caches these layers, so when you rebuild an image, it reuses unchanged layers instead of rebuilding everything from scratch.

3. **Faster Builds**: By using cached layers, Docker significantly speeds up the build process for parts that haven't changed.

4. **Cache Invalidated by Changes**: If a layer changes (e.g., the content of a `COPY` command), all subsequent layers need to be rebuilt, starting from that point.

    
## Docker Compose

1. **Multiple Containers**: Docker Compose allows you to define and run multiple containers as a single application using a `docker-compose.yml` file.

2. **Service Definition**: Each container is defined as a "service" in the YAML file, specifying its image, volumes, networks, and other configurations.

3. **Simplified Management**: You can manage all containers together (start, stop, build) with a single command like `docker-compose up` and `docker-compose down`.

4. **Environment Configuration**: Easily manage environment variables, networks, and volumes between multiple services, making development and deployment consistent.

5. **Isolation and Orchestration**: Compose helps isolate environments and orchestrate container interactions, making it easy to spin up complex multi-container environments.
 

##  Docker network
> Three main types of network:
> 1.bridge
> 2.host
> 3.none

> *we use it to connect two container under same network*

- **To show networks** : docker network ls

- **To inspect specific network**: docker network inspect milkyway

- **To create own network**: docker network create -d bridge -network_name- (eg: youtube)

- **To run on specific network**: docker run -it --network=milkyway --name wanda busybox
