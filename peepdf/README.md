# Powerful Python tool to analyze PDF documents.

## Input

```
PDF
```

## Output

```
Peepdf report (XML, JSON)
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*peepdf/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/peepdf/Dockerfile))


## Usage



***1.a) Pull the docker image*** 

```
docker pull cincan/peepdf
```

***1.b) Or clone the repository and build***

```
git clone https://gitlab.com/cincan/tools.git
cd tools/peepdf/
docker build . -t cincan/peepdf
```

***2. Run the docker container***  

Example 1. Analyze a PDF file:

`$ docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf -f`

Example 2. Interactive mode

`$ docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf -f -i`

Example 3. Use the cincan command line tool, check hash from VirusTotal

`$ cincan run cincan/peepdf samples/testfile.pdf -f -c`  


## Project homepage

[https://github.com/jesparza/peepdf](https://github.com/jesparza/peepdf)


### License

[GNU General Public License v3.0](https://github.com/jesparza/peepdf/blob/master/COPYING)
