# "Firmware Analysis Tool"

Binwalk with all optional run-time dependencies.

## Supported tags and respective `Dockerfile` links

* `latest` 
([*binwalk/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/binwalk/Dockerfile))

## Input

```
binary
```

## Output

```
Binwalk report
```

## Usage

***Binwalk help***

`$ docker run cincan/binwalk --help`

***Binwalk basic usage***

`$ docker run -v /samples:/samples cincan/binwalk /samples/firmware.bin`

## Project homepage

https://github.com/ReFirmLabs/binwalk
