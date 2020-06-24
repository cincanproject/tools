# PDF X-RAY Lite: Release 1.0

PDF X-Ray Lite is a lightweight version of PDF X-Ray used to analyze PDF files for malicious objects. 


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
([*pdfxray-lite/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/pdfxray-lite/Dockerfile))

## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd dockerfiles/pdfxray-lite/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/pdfxray_lite
docker pull cincan/pdfxray-lite
```

***3. Run the docker container***

***Usage for one file, write results to a report file***  

`$ docker run -v /samples:/samples cincan/pdfxray-lite -f /input/sample.pdf -r 
/output/report`  

***Analyze all files in a directory***  

`$ docker run -v /samples:/samples cincan/pdfxray-lite -d /input/ -r /output/report`

***Run with cincan command***

`$ cincan run cincan/pdfxray-lite -f input/sample.pdf -r output/report`

## Project homepage

https://github.com/9b/pdfxray_lite.git
