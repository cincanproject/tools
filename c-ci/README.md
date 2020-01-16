# Concourse CI

The Concourse CI is an Ubuntu 18.04 based image that can be used alongside with 
Concourse Worker and PostreSQL images to deploy Concourse.

## Supported tags and respective `Dockerfile` links

* `latest` 
([*c-ci/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/c-ci/Dockerfile))

## Docker Compose file

Following Docker Compose file can be used to build Concourse CI and Concourse worker 
containers along with [PostgreSQL](https://hub.docker.com/_/postgres) database 
container. However, the CinCan project recommends that you try our pilot environment 
and it's automated builder before you build the environment using the following 
Docker Compose file. Pilot environment repository: https://gitlab.com/CinCan/pilot .

```yml
# USAGE
# 
--------------------------------------------------------------------------------------------------------------------------------
# 1. Replace $VARIABLES
# 
--------------------------------------------------------------------------------------------------------------------------------
# 2. Create required keys
# $ mkdir -p /opt/cincan/keys
# $ ssh-keygen -t rsa -m pem -q -N '' -f /opt/cincan/keys/tsa_host_key
# $ ssh-keygen -t rsa -m pem -q -N '' -f /opt/cincan/keys/worker_key
# $ ssh-keygen -t rsa -m pem -q -N '' -f /opt/cincan/keys/session_signing_key
# $ cp /opt/cincan/keys/worker_key.pub /opt/cincan/keys/authorized_worker_keys
# 
--------------------------------------------------------------------------------------------------------------------------------
# 3. Build the environment
# $ docker-compose up -d
# 
--------------------------------------------------------------------------------------------------------------------------------
# 4. Browse to http://$URL:8080 to see the GUI
# 
--------------------------------------------------------------------------------------------------------------------------------
# 5. Use Fly CLI
# $ docker exec -it concourse-ci fly --help
# 
--------------------------------------------------------------------------------------------------------------------------------

version: "3.5"

services:

  concourse-db:
    image: postgres
    container_name: concourse-db
    networks:
    - cincan
    environment:
    - POSTGRES_DB=$DATABASE
    - POSTGRES_PASSWORD=$PASSWORD
    - POSTGRES_USER=$USERNAME

  concourse-ci:
    image: cincan/c-ci
    command: web
    container_name: concourse-ci
    depends_on: [concourse-db]
    networks:
    - cincan
    ports:
    - "8080:8080"
    volumes:
    - "/opt/cincan/keys:/etc/concourse"
    environment:
    - CONCOURSE_EXTERNAL_URL=$URL
    - CONCOURSE_POSTGRES_USER=$USERNAME
    - CONCOURSE_POSTGRES_PASSWORD=$PASSWORD
    - CONCOURSE_POSTGRES_DATABASE=$DATABASE
    - CONCOURSE_MAIN_TEAM_LOCAL_USER=$USERNAME
    - CONCOURSE_ADD_LOCAL_USER=$USERNAME:$PASSWORD
    - CONCOURSE_SESSION_SIGNING_KEY=/etc/concourse/session_signing_key
    - CONCOURSE_TSA_HOST_KEY=/etc/concourse/tsa_host_key
    - CONCOURSE_TSA_AUTHORIZED_KEYS=/etc/concourse/authorized_worker_keys
    - CONCOURSE_POSTGRES_HOST=concourse-db
    - CONCOURSE_WORK_DIR=/opt/concourse/worker
    - CONCOURSE_TSA_WORKER_PRIVATE_KEY=/etc/concourse/worker_key
    - CONCOURSE_TSA_PUBLIC_KEY=/etc/concourse/tsa_host_key.pub

  concourse-worker:
    image: cincan/c-worker
    command: worker
    container_name: concourse-worker
    depends_on: [concourse-ci]
    privileged: true
    networks:
    - cincan
    volumes:
    - "/opt/cincan/keys:/etc/concourse"
    - "/opt/cincan/concourse:/opt/concourse"
    environment:
    - CONCOURSE_SESSION_SIGNING_KEY=/etc/concourse/session_signing_key
    - CONCOURSE_TSA_HOST_KEY=/etc/concourse/tsa_host_key
    - CONCOURSE_TSA_AUTHORIZED_KEYS=/etc/concourse/authorized_worker_keys
    - CONCOURSE_GARDEN_DNS_SERVER=$DNS
    - CONCOURSE_WORK_DIR=/opt/concourse/worker
    - CONCOURSE_TSA_WORKER_PRIVATE_KEY=/etc/concourse/worker_key
    - CONCOURSE_TSA_PUBLIC_KEY=/etc/concourse/tsa_host_key.pub
    - CONCOURSE_TSA_HOST=concourse-ci:2222

networks:
  cincan:
```

## Project homepage

https://github.com/concourse
