# PDFexaminer  

Upload a PDF to www.pdfexaminer.com/pdfapi.php and get results.

## Build:
```
docker build -t cincan/pdfexaminer .
```

## Usage:
```
docker run -v /samples:/samples cincan/pdfexaminer /samples/input/sample.pdf [options]  

[options] = output format (default json)

```

