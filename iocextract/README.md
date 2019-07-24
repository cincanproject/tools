# "Advanced Indicator of Compromise (IOC) extractor"

Extracts urls, hashes (md5, sha1, sha256, sha512), emails and ips from a file.

## Input

```
File
```

## Output

```
Iocextract report. Writes results in seperate directories under given output directory.
```


## Supported tags and respective `Dockerfile` links

* `latest` 
([*iocextract/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/iocextract/Dockerfile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd dockerfiles/iocextract
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/iocextract
docker pull cincan/iocextract
```

***3. Run the docker container***

Load all files from /files/ and extracts hashes:  

`$ docker run -v $(pwd):/files cincan/iocextract --output /files/output/ --path /files/ --hash`  

Load specific file from mounted volume and exracts emails, urls:  

`$ docker run -v $(pwd):/files cincan/iocextract --output /files/output/ --path /files/file -u -e`


***Options***  

```  
[--verbose, -v] Sets verbosity to high, prints lists of found urls and hashes
[--url, -u] Extracts urls
[--hash] Extracts hashes (md5, sha1, sha256, sha512)
[--email, -e] Extracts emails
[--ip, -i] Extracts ips (ipv4, ipv6)
```

## Project homepage

https://github.com/InQuest/python-iocextract
