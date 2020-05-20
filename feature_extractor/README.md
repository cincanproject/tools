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

1. Run once to create API.json, active_analyzers -list and other configuration files:

`$ docker run -v $(pwd):/data fe --path /data/`  

2. Edit _active_analyzers_ file to select which analyzers to use  

3. Run again to add chosen analyzers to API.json:  

`$ docker run -v $(pwd):/data fe --path /data/`  

4. Add API keys to API.json, then run analysis:  

Analyse a file in directory "/samples":  

`$ docker run --rm -v /samples:/samples cincan/feature_extractor -v /samples/iocslist --path /samples/`  

Analyse a list of iocs in jsonl format:  

`$ docker run -v $(pwd):/data cincan/feature_extractor --path /data/ --injsonl /data/jsonl_input`  

Using cincan-command, open results to a browser window:  

`cincan run cincan/feature_extractor --confpath . --path . --injsonl jsonl_input --browser`  


***Options***
```  
usage: analyze_parallel.py [-h] [--infile INFILE] [--injsonl INJSONL]
                           [--file FILE] [--ip IP] [--domain DOMAIN]
                           [--fqdn FQDN] [--hash HASH] [--mail MAIL]
                           [--other OTHER] [--url URL] [--iocp IOCP]
                           [--update] [--browser] [--confpath CONFPATH]
                           [--path PATH]
```

## Project homepage

[https://gitlab.com/CinCan/feature_extractor/](https://gitlab.com/CinCan/feature_extractor/)

