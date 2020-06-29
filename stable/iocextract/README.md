# Advanced Indicator of Compromise (IOC) extractor

Extracts urls, hashes (md5, sha1, sha256, sha512), emails and ips from a file. By default, all types are attempted to be detected.

## Input

```
File, STDIN
```

## Output

```
Iocextract report. By default results are printed into STDOUT line by line. 
```

## Usage

***1. Use [cincan-command](https://gitlab.com/cincan/cincan-command)***

Note that `-t` flag must be provided to act as pseudo-tty. Otherwise output is not printed to STDOUT if no other output defined.

```
cincan run -t cincan/iocextract --input ioc_test.pdf
```


***2. Run the docker container***

Using volume mounts to get file inside container:

```
docker run -tv $(pwd):/files cincan/iocextract --input /files/ioc_test.pdf
```  


Use `--help` to see all available options of the tool or consult project home page.

## Project homepage

https://github.com/InQuest/python-iocextract

## Licence

GNU GPL v2