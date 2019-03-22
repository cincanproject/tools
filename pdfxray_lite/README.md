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
* `latest` 
([*pdfxray_lite/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/pdfxray_lite/Dockerfile))

## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/dockerfiles
cd dockerfiles/pdfxray_lite/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/pdfxray_lite
docker pull cincan/pdfxray_lite
```

***3. Run the docker container***

***Usage for one file, write results to a report file***  

`$ docker run -v /samples:/samples cincan/pdfxray_lite -f /input/sample.pdf -r 
/output/report`  

***Analyze all files in a directory***  

`$ docker run -v /samples:/samples cincan/pdfxray_lite -d /input/ -r /output/report`

## Project homepage

https://github.com/9b/pdfxray_lite.git
