#!/bin/bash

docker rm spark-worker-1 spark-worker-2 spark-master spark-history
docker image rm spark-base spark-master spark-worker spark-history
docker image prune -f