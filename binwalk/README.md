# Binwalk with all optional run-time dependencies

## Usage:

### Use existing image:
```
docker pull cincan/binwalk
```

### Or build image locally from Dockerfile:
```
docker build . --tag cincan/binwalk
```

### Run the container using the image:
```
docker run -v /samples:/samples cincan/binwalk /samples/firmware.bin
```

## Optimization:
 - Find out how Binwalk with all optional run-time dependencies can be installed on Alpine
