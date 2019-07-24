# "Analyze suspicious files and URLs to detect types of malware"

Retrieves file or url results from VirusTotal.  
By default only sends hash of a file to check if the file has already been analyzed.  
It's possible to send the whole file if report doesn't exist with --send argument

## Input
`
any file
`

## Output

`
Virustotal report
`

## Supported tags and respective `Dockerfile` links

* `latest` 
([*virustotal/Dockerfile*](https://gitlab.com/CinCan/Tools/blob/master/pipelines/dockerfiles/virustotal/Dockerfile))

## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/virustotal/
```

***2. Build OR pull the docker image***

```
docker build . -t cincan/virustotal
docker pull cincan/virustotal
```

***3. Run the docker container***

Scans all urls in the newline delimited file:  

`$ docker run -v /files:/files cincan/virustotal --output /files/ --url_file /files/url_file [options]`  

Scans all files in the folder:  

`$ docker run -v /files:/files cincan/virustotal --output /files/ --files /files/ [options]`

## Options

`
[--send, -s] Sends file or url to be analyzed if existing report doesn't exist
[--verbose, -v] Sets verbosity to high
`

## Project homepage

https://github.com/VirusTotal
