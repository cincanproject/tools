# "Visualizing webserver's access log data to help detecting malicious activity"

## Input

```
access.log (Apache)
```

## Output

```
output.html
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*access-log-visualization/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/access-log-visualization/Dockerfile))

## Usage


***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/dockerfiles.git
cd dockerfiles/access-log-visualization
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/access-log-visualization
docker pull cincan/access-log-visualization
```

***3. Run the docker container***
```
docker run -v "$PWD/samples":/samples cincan/access-log-visualization
```

## Project homepage

https://jupyter.org/

