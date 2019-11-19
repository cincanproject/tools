# Feature_extractor

A tool for running Cortex-analyzers from command line and parsing and printing results to a configurable HTML report.

## Input

```
list of possible IoCs
```

## Output

```
outputs of Cortex-analyzers
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*feature_extractor/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/feature_extractor))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/feature_extractor/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/feature_extractor
docker pull cincan/feature_extractor
```

***3. Run the docker container***

Analyse a file in directory "/samples":

`$ docker run --rm -v /samples:/samples cincan/feature_extractor -v /samples/iocslist`  



***Options***
```  
usage: analyze_parallel.py [-h] [--infile INFILE] [--injsonl INJSONL]
                           [--file FILE] [--ip IP] [--domain DOMAIN]
                           [--fqdn FQDN] [--hash HASH] [--mail MAIL]
                           [--other OTHER] [--url URL] [--iocp IOCP]
                           [--update]
```

## Project homepage

[https://gitlab.com/CinCan/wp1/tree/master/feature_extractor](https://gitlab.com/CinCan/wp1/tree/master/feature_extractor)
