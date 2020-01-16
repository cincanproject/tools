# PDFExaminer

## Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results

## Input

```
PDF files
```

## Output

```
PDFExaminer report  

json,ioc,xml,php...
```


## Supported tags and respective `Dockerfile` links
* `latest` 
([*pdfexaminer/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/pdfexaminer/Dockerfile))

## Usage


***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/pdfexaminer
```

***2. Build OR pull the docker image***

```
docker build . -t cincan/pdfexaminer
docker pull cincan/pdfexaminer
```

***3. Run the docker container***

Analyse a sample in directory "/samples":

`$ docker run -v /samples:/samples cincan/pdfexaminer /samples/input/sample.pdf  
[OUTPUT FORMAT(default JSON)]`


## Project homepage

https://github.com/mwtracker/pdfexaminer_tools
