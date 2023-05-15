#!/bin/bash

mkdir -p logs

# # Building dev container image
# echo "================================================"
# echo "Building dev container image"
# docker build \
#   -f docker/Dockerfile.devcontainer \
#   -t python-310-devcontainer docker/
# echo "Finished building devcontainer image"

# Create the docker network for the stack
echo "================================================"
echo "Creating docker network"
docker network create -d bridge hadoop_local_cluster
echo "Finished creating docker network"