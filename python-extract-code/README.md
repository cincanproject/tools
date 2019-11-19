# Extract code

Extract python based binary code

## Input

```
PE
```

## Output

```
python
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*python-extract-code/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/python-extract-code))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/python-extract-code/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/python-extract-code
docker pull cincan/python-extract-code
```

***3. Run the docker container***

Try to extract a file in directory "/samples":

`$ docker run --rm -v /samples:/samples cincan/python-extract-code /samples/binary`  



***Options***
```  
usage: extract_code.py [-h] inpath

Extract Python code from Python compiled EXE

positional arguments:
  inpath      Path to file or folder containing files

optional arguments:
  -h, --help  show this help message and exit
```

## Project homepage

[https://gitlab.com/CinCan/tools/tree/master/python-extract-code](https://gitlab.com/CinCan/tools/tree/master/python-extract-code)
