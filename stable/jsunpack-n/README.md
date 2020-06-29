# Jsunpack-n - Emulates browser functionality, detect exploits etc.

Emulates browser functionality when visiting an URL. Detects browser exploits, scans PDF.

## Input

```
PDF, URL, PCAP, JavaScript, SWF
```

## Output

```
report, shellcode/other suspicious content
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*jsunpack-n/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/jsunpack-n/Dockerfile))


## Usage 


***1. Clone the repository***  

```
git clone https://gitlab.com/CinCan/tools.git
cd tools/jsunpack-n/
```

***2. Build OR pull the docker image***  

```
docker build . -t cincan/jsunpack-n
docker pull cincan/jsunpack-n
```

***3. Run the docker container***  


Example 1. File scan  

`$ docker run -v $(pwd):/data cincan/jsunpack-n /data/samples/testfile.pdf -V -d /data/samples/output/`

Example 2. Url scan  

`$ docker run -v $(pwd):/samples cincan/jsunpack-n -u https://<TARGET.URL> -V -d /samples/output`

Example 3. Run jsunpack-n with the cincan command line tool  

`$ cincan run cincan/jsunpack-n samples/testfile.pdf -V -d result-dir`  


## Project homepage

[https://github.com/urule99/jsunpack-n](https://github.com/urule99/jsunpack-n)


## License

[GNU General Public License v2.0](https://github.com/urule99/jsunpack-n/blob/master/COPYING)
