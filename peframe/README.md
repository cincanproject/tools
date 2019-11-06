# PEframe

An open source tool to perform static analysis on Portable Executable malware and malicious MS Office documents. 

## Input

```
PE
```

## Output

```
json
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*peframe/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/peframe))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/peframe/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/peframe
docker pull cincan/peframe
```

***3. Run the docker container***

Analyze a file in directory "/samples":

`$ docker run --rm -v /samples:/samples cincan/peframe /samples/sample`  



***Options***
```  
usage: peframe [-h] [-v] [-i] [-x XORSEARCH] [-j] [-s] file

Tool for static malware analysis.

positional arguments:
  file                  sample to analyze

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i, --interactive     join in interactive mode
  -x XORSEARCH, --xorsearch XORSEARCH
                        search xored string
  -j, --json            export short report in JSON
  -s, --strings         export all strings

api_config: /usr/lib/python3.7/site-packages/peframe-6.0.3-py3.7.egg/peframe/config/config-peframe.json
string_match: /usr/lib/python3.7/site-packages/peframe-6.0.3-py3.7.egg/peframe/signatures/stringsmatch.json
yara_plugins: /usr/lib/python3.7/site-packages/peframe-6.0.3-py3.7.egg/peframe/signatures/yara_plugins
```

## Project homepage

[https://github.com/guelfoweb/peframe](https://github.com/guelfoweb/peframe)
