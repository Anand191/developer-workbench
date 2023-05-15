# developer-workbench

Providing a suite of docker based setups for local development and testing in a production environment. Currently the following stacks are available:

- Hadoop - Hive - Spark - Python dev environment with Pyspark installed
- ELK - Spark - Jupyterlab dev environment with Pyspark installed

## Dependencies

- Docker Engine - Ubuntu 22.04
- Docker Desktop - Mac
- Docker Desktop with WSL2 Backend - Windows >=10
- Git Bash - Windows only

Note: Run all the following commands on Windows from Git Bash if using Windows filesystem. If using WSL2 terminal execute the linux instructions directly.

## Hadoop-Hive-Spark-Python

This stack starts a hadoop-hive-spark cluster and a python dev environment (with necessary libraries pre-installed) on the same docker network to facilitate inter service communication.

Please not I use a docker-compose.yml for the devcontainer instead of just the dockerfile since I wanted to retain the flexibility of adding more services to the dev compose file (e.g. a front end server) if needed/when I want to extend this setup.

**NOTE:** Execute these commands from the root folder and On Windows please run all the following commands from WSL

### Init steps

This builds the docker image for the devcontainer as well as creates the docker network which these services will use.

```
$ ./prerequisites.sh
```

### Start the compute stack

Start the namenode, datanode, hive-server, hive-metastore, spark-master and spark-workers

```
$ cd hadoop && docker compose up
```

You can use any client such as docker desktop or [portainer](https://www.portainer.io/) to manage the containers from a UI interface

### Add some data to hdfs

The instructions for this step have been picked from [this blog](https://hshirodkar.medium.com/apache-hive-on-docker-4d7280ac6f8e).

- Log into the hive server as follows. Or use docker desktop or portrainer to open an exec console

```
$ docker exec -it hive-server /bin/bash
```

- Create a hive table for weather data using the included hql

```
$ cd .. && cd hive_db
$ hive -f weather_table.hql
$ hadoop fs -put weather.csv hdfs://namenode:8020/user/hive/warehouse/testdb.db/weather
```

Validate the setup by navigating to http://localhost:9870/explorer.html#/user/hive/warehouse/testdb.db and verifying that the _weather_ table has been create.

### Testing the setup using PySpark

Pre-requisite for this step is having **Dev Containers** installed in vscode. Following steps are for vscode:

- `Ctrl+Shift+P` &Rarr; Dev Containers: Open Folder in Container
- Open &harr;`notebooks/test_spark.ipynb`&harr; and fire away!!

### Advanced Usage: Using git from inside the devontainer

Pre-requisite for this step is having ssh key confiured for your host user for your github/gitlab etc. Your ssh key gets forwarded to the devcontainer (nonroot) user but there is an issue with _known_hosts_.

- Fire up a terminal from inside the devcontainer &harr;`vim ~/.ssh/known_hosts`&harr; and replace the existing content there with the following:

```
github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=
github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk=
```
