# PDF-parser

PDF-parser tool will parse a PDF document to identify the fundamental elements used in the analyzed file

## Input

```
PDF
```

## Output

```
PDF-parser report
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*pdf-parser/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/pdf-parser))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/pdf-parser/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/pdf-parser
docker pull cincan/pdf-parser
```

***3. Run the docker container***

Example 1. Analyze a file in directory "/samples":

`$ docker run --rm -v /samples:/samples cincan/pdf-parser /samples/sample.pdf -a`  


Example 2. Analyze a file through filters, and display content for objects withouth streams:  

`$ docker run --rm -v /samples:/samples cincan/pdf-parser /samples/sample.pdf -c --filter`   


Example 3. Run with the cincan command line tool, using &Hex decoder:  

`cincan run pdf-parser ^/samples/sample.pdf -c --filter --decoders=decoder_ah.py`


```

## Project homepage

[https://github.com/DidierStevens/DidierStevensSuite](https://github.com/DidierStevens/DidierStevensSuite)
