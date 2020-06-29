# PEframe - static analysis for PE executables and MS office documents

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

### Install

***Method 1: Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/peframe/
docker build . -t cincan/peframe
```

***Method 2: Pull the docker image*** 

```
docker pull cincan/peframe
```

***Method 3: use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool***

Follow `cincan` tool installation steps. If this tool is used, no need to install `peframe` separately.

### Running

***Method 1. Run the docker container***

Analyze a file in directory "/samples":

`$ docker run --rm -v /path/to/samples:/samples cincan/peframe /samples/peframe_sample.exe`  

***Method 2. Run with ['cincan'](https://gitlab.com/CinCan/cincan-command) tool:***

Analyze the example sample available in the sample folder:

`$ cincan run cincan/peframe samples/peframe_sample.exe`

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

### Testing

Couple of tests are included for testing the functionality of the container. Tox can be used for testing this tool (run from the root of this repository);
```
pip install tox
tox peframe
```

### Sample file

Sample file was created for CriM-2019 workshop (Compiled binary C# .NET Assembly). It contains a simple dropper for malicious binary from remote URL.

## Project homepage

[https://github.com/guelfoweb/peframe](https://github.com/guelfoweb/peframe)

## License

GNU General Public License
