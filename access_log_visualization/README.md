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

* `latest` ([*access_log_visualization/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/access_log_visualization/Dockerfile))

## Usage


***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/dockerfiles.git
cd dockerfiles/access_log_visualization
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/access_log_visualization
docker pull cincan/access_log_visualization
```

***3. Run the docker container***
```
docker run -v "$PWD":/samples cincan/access_log_visualization
```

## Project homepage

https://jupyter.org/

