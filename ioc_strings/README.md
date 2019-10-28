# IOC strings

Extracts urls, hashes, emails, ips, domains and base64 (other) from a file.

## Input

```
File/Directory
```

## Output

```
jsonl format when using "-t" option
```


## Supported tags and respective `Dockerfile` links

* `latest` 
([*ioc_strings/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/ioc_strings/Dockerfile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd ioc_strings
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/ioc_strings
docker pull cincan/ioc_strings
```

***3. Run the docker container***

## Project homepage

https://gitlab.com/CinCan/ioc_strings
