#!/bin/bash

docker rm spark-worker-1 spark-worker-2 spark-master spark-history front_end jupyterlab es01 kib01
docker image rm spark-base spark-master spark-worker spark-history jupyterlab front_end cluster-base docker.elastic.co/elasticsearch/elasticsearch docker.elastic.co/kibana/kibana
docker image prune -f