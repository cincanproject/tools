# Ssdeep based clustering tool

ssdeep Cluster clusters files using ssdeep as a comparison algorithm.

## Input

```
*
```

## Output

```
tar (groups.json & .gexf)
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*ssdc/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/ssdc/Dockerfile))


## Usage


***Pull the docker image*** 

```
docker pull cincan/ssdc
```

***OR build the dockerfile***

```
git clone https://gitlab.com/CinCan/tools.git
cd tools/ssdc
docker build . -t cincan/ssdc
```


***Run the docker container***  

Example 1. Group files in current folder:

`$ docker run -v $(pwd):/data cincan/ssdc /data -o /data/output.tar`

Example 2. Running with the cincan tool:

`$ cincan run cincan/ssdc * -o output.tar`



## Project homepage

[https://github.com/bwall/ssdc](https://github.com/bwall/ssdc)


### License

[MIT License](https://github.com/bwall/ssdc/blob/master/LICENSE)
