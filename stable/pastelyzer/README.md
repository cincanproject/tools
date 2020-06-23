# "the paste analyzer"

`pastelyzer` analyzes text documents for interesting security and privacy
related *artefacts*. Also analyzes embedded binary (eg. base64) content recursively.

See the original [README](https://github.com/cert-lv/pastelyzer) for more information

Currently the container only supports the interactive mode

## Input

```
text
```

## Output

```
pastelyzer report
```


## Supported tags and respective `Dockerfile` links

* `latest` 
([*pastelyzer/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/pastelyzer/Dockerfile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools.git
cd tools/pastelyzer
```

***2. Build OR pull the docker image***

```
docker build . -t cincan/pastelyzer
docker pull cincan/pastelyzer
```

***3. Run the docker container***  

Example 1. Read a text file from stdin  

`$ docker run --rm -i cincan/pastelyzer - < data.txt`  

Example 2. Read a text file from stdin with the CinCan command   

`$ cincan run cincan/pastelyzer - < data.txt`  

Example 3. Read a text file as argument with the CinCan command   

`$ cincan run cincan/pastelyzer data.txt`  

## Project homepage

https://github.com/certlv/pastelyzer

