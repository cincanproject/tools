# "A Program to analyse OLE files."

## Input

```
.doc, .xls, .ppt
```

## Output

```
oledump report
JSON
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*oledump-linux/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/oledump-linux/Dockerfile))

## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools.git
cd tools/oledump-linux
```

***2. Build OR pull the docker image***

```
docker build . -t cincan/oledump-linux
docker pull cincan/oledump-linux
```

***3. Run the docker container***  

Example 1. List streams  

`$ docker run --rm -v $(pwd):/input cincan/oledump-linux /input/samples/testfile.docm`  

Example 2. Identify encryption version  

`$ docker run --rm -v $(pwd):/input cincan/oledump-linux -p plugin_office_crypto /input/samples/testfile.docm`  

Example 3. Dump a stream's content using the CinCan command line tool:    

`$ cincan run cincan/oledump-linux -s <STREAM NUMBER> samples/testfile.docm`  


## Project homepage

https://blog.didierstevens.com/programs/oledump-py/

