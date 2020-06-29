# osslsigncode

# "OpenSSL based Authenticode signing for PE/MSI/Java CAB files"

## Input

```
exe/sys/dll
```

## Output

```
signed pe / verification report / ...
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*osslsigncode/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/osslsigncode))


## Usage


***Pull the docker image*** 

```
docker pull cincan/osslsigncode
```

***OR build the dockerfile***

```
git clone https://gitlab.com/CinCan/tools.git
cd tools/osslsigncode/
docker build . -t cincan/osslsigncode
```

***Run the docker container***

Example 1. Verify a file in current folder using docker:

`$ docker run -v $(pwd):/data cincan/osslsigncode verify /data/file.exe`


Example 2. Running with the ***cincan*** tool. Verify file using a specified crt file:

`$ cincan run cincan/osslsigncode verify -CAfile /usr/lib/ssl/certs/ca-certificates.crt -in file.exe`



## Project homepage

[https://github.com/mtrojnar/osslsigncode](https://github.com/mtrojnar/osslsigncode)
