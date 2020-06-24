# Visualizing webserver's access log data to help detecting malicious activity

## Input

```
access.log (Apache)
```

## Output

```
output.html
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*access-log-visualization/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/access-log-visualization/Dockerfile))

## Usage


***1.a) Clone the repository and build docker image***

```
git clone https://gitlab.com/CinCan/tools.git
cd dockerfiles/access-log-visualization
docker build . -t cincan/access-log-visualization
```

***1.b) Pull the docker image*** 

```
docker pull cincan/access-log-visualization
```

***2. Run the tool***
```
cincan run cincan/access-log-visualization -i samples/access.log
```

```
docker run --rm -v $(pwd):/data cincan/access-log-visualization -i /data/samples/access.log -o /data/output-folder
```

## Project homepage

https://jupyter.org/

