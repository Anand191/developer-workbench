## ELK-Spark-Jupyterlab

Pick and choose components from the compose file to build a separate stack

### Build Docker images

This builds all the necessary folders and images needed for the setup. Run it from the room folder

```
./build_images.sh
```

### Get Data

After running the above build script place your data inside **/shared_vol/data** folder

### Start application

- the **shared_vol/** folder is shared between dockers and host filesystem

- to start the workbench on Mac/Linux run the following in terminal

```
SHARED_DIR=`pwd`/shared_vol docker-compose -f docker-compose.yml up
```

- to start the workbench on Windows run the following in terminal

```
SHARED_DIR=~/path/to/developer-workbench/shared_vol docker-compose -f docker-compose-windows.yml up
```

### Application URLs

- [JupyterLab](http://localhost:8888)
- [Bokeh UI](http://localhost:5006)
- [Elasticsearch](http://localhost:9200)
- [Kibana](http://localhost:5601)
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

### Cleanup Docker env

Removes all stopped containers and deletes images with intermediate layers.

```
./cleanup-docker.sh
```

### Notes and Troubleshooting

- This setup has been tested on windows only for Docker with WSL2 backend
- The services that you need can be selected in the docker-compose file(s). Unnecessary services can simply be commented out before starting docker-compose
- The ELK stack in docker-compose might throw a Max Virtual memory areas vm.max_map_count is too low error. Solution can be found at the following link for both Mac and Windows:
- https://stackoverflow.com/questions/51445846/elasticsearch-max-virtual-memory-areas-vm-max-map-count-65530-is-too-low-inc
