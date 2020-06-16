# Identify-file

Identifies file type using several techniques

## Supported tags and respective `Dockerfile` links

* `latest` 
([*identify-file/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/identify-file))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/identify-file
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/identify-file
docker pull cincan/identify-file
```

***3. Run the docker container***

Analyse a sample in directory "/samples":  

`$ docker run -v /samples:/samples cincan/identify-file /samples/sample`


