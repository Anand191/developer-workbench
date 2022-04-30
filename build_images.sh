#!/bin/bash

mkdir -p shared-vol/history
mkdir -p shared-vol/logs
mkdir -p shared-vol/data
mkdir -p shared-vol/notebooks

# -- Software Stack Version

SPARK_VERSION="3.2.0"
HADOOP_VERSION="3.2"
JUPYTERLAB_VERSION="3.3.4"

# -- Building the Images

docker build \
  -f docker/Dockerfile.cluster_base \
  -t cluster-base docker/

docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg hadoop_version="${HADOOP_VERSION}" \
  -f docker/Dockerfile.spark_base \
  -t spark-base docker/

docker build \
  -f docker/Dockerfile.spark_master \
  -t spark-master docker/

docker build \
  -f docker/Dockerfile.spark_history \
  -t spark-history docker/

docker build \
  -f docker/Dockerfile.spark_worker \
  -t spark-worker docker/

docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg jupyterlab_version="${JUPYTERLAB_VERSION}" \
  -f docker/Dockerfile.jupyter_lab \
  -t jupyterlab docker/

docker build \
  -f docker/Dockerfile.front_end 
  -t front_end .