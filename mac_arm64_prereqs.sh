#!/bin/bash

# Building dev container image
echo "================================================"
echo "Building hive metastore postgres container image for arm64"
docker build \
  -f Dockerfile.hive_metastore \
  -t bde2020/hive-metastore-postgresql:2.3.0 data/hive-metastore-postgres/
echo "Finished building hive postgres metastore image"
