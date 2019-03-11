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

```
git clone https://gitlab.com/CinCan/dockerfiles.git
cd dockerfiles/access_log_visualization
docker pull cincan/access_log_visualization
docker run -v "$PWD":/samples cincan/access_log_visualization
```

## Project homepage

https://jupyter.org/

