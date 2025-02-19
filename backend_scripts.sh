#!/bin/bash

# Contains functional scripts to setup the backend application


# Globals
backend_docker_image_name="kig_backend"


# build docker image of backend application
build_backend_docker_image()
{
    if ! cd backend; then
        echo "Error: backend directory not found"
        return 1
    fi
    
    if ! docker build -t "$backend_docker_image_name" .; then
        echo "Error: Docker build failed"
        cd ..
        return 1
    fi
    
    cd ..
    echo "Successfully built $backend_docker_image_name docker image"
}

run_backend_container()
{
    container_name="kig_container"
    
    # Check if container exists and remove it
    if docker ps -a --format '{{.Names}}' | grep -q "^${container_name}$"; then
        echo "Container ${container_name} exists. Removing it..."
        docker rm -f ${container_name}
    fi
    
    # Run new container with name "kig_container"
    if ! docker run --name kig_container -p 8000:8000 --env-file .env $backend_docker_image_name; then
        echo "Error: Failed to run docker container"
        return 1
    fi
    
    echo "Successfully ran docker container --> $container_name"
}


# Runs database locally using port 5434 on the user "kig_franz" (feel free to change to your postgresql user)
run_postgresql_db()
{
    psql -h localhost -p 5434 -U kig_franz -d keep_it_green
}


# display all available functions in this script
list_functions()
{
    echo "Available functions:"
    echo "  - build_backend_docker_image"
    echo "  - run_backend_container"
    echo "  - run_postgresql_db"
}


# show if no arguments were specified
if [ $# -eq 0 ]; then
    echo "Usage: $0 <function_name>"
    list_functions
    exit 1
fi


# check if the argument inputted exists
if declare -f "$1" > /dev/null; then
    "$1"
else
    echo "Unknown function: $1"
    list_functions
    exit 1
fi
