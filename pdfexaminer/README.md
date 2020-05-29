## Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results

## Input

```
PDF files
```

## Output

```
json,ioc,xml,php
```


## Supported tags and respective `Dockerfile` links
* `latest`
([*pdfexaminer/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/pdfexaminer/Dockerfile))

## Usage

Get help, using the [`cincan`](https://gitlab.com/cincan/cincan-command) tool:
```bash
cincan run cincan/pdfexaminer --help
```

Analyze a PDF:

```bash
cincan run cincan/pdfexaminer --input /samples/sample.pdf --format xml

    or with docker:

docker run -v /samples:/samples cincan/pdfexaminer --input /samples/sample.pdf --format json
```

## Project homepage

https://github.com/mwtracker/pdfexaminer_tools  
Python API: https://gitlab.com/cincan/pdfexaminer  
