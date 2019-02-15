# Analyze PDF files

## Input

```
PDF
```

## Output

```
HTML
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*pdfxray_lite/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/pdfxray_lite/Dockerfile))


## Usage


***Usage for one file, write results to a report file***  
```
$ docker run -v /samples:/samples cincan/pdfxray_lite -f /input/sample.pdf -r /output/report
```

***Analyze all files in a directory***  

```
docker run -v /samples:/samples cincan/pdfxray_lite -d /input/ -r /output/report
```


## Project homepage

https://github.com/9b/pdfxray_lite.git