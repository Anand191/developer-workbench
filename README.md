# developer-workbench

Setup a quick to spin up workbench with docker with the possibility to select services

## Build Docker images

This builds all images needed for the setup.

```
./build_images.sh
```

## Prepare environment

This script creates required directories, which are used by the setup.

```
./setup_env.sh
```

## Start application

```
# this directory will be shared among Spark and Jupyter services
mkdir ./shared-vol

# download data, specify --with-csv if you want to download and unzip data in csv format (100Gb) as well
cd shared-vol
../collect-data.sh

# this will start Docker compose application
SHARED_DIR=`pwd`/shared_vol docker-compose up
```

## Application URLs

- [JupyterLab](http://localhost:8888)
- [Spark master](http://localhost:8080/home)
- [Spark worker I](http://localhost:8081)
- [Spark worker II](http://localhost:8082)
- [Spark Application UI](http://localhost:4040)
- [Spark history](http://localhost:18080)
- [SparkLint](http://localhost:23763)

### Restart SparkLint to get new logs

Sparklint doesn't fetch new logs automatically. To process new logs you can either add them manually through UI or restart Sparklint docker component

```
docker-compose -f docker-compose.yml restart sparklint
```

## Cleanup Docker env

Removes all stopped containers and deletes images with intermediate layers.

```
./cleanup-docker.sh
```
