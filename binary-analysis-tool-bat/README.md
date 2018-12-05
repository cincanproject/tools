# Binary Analysis Tool BAT with extratools

## Usage:

### Use existing image:
```
docker pull cincan/binary-analysis-tool-bat
```

### Or build image locally from Dockerfile:
```
docker build . --tag cincan/binary-analysis-tool-bat
```

### Run the container using the image for one sample:
```
docker run -v /samples:/samples cincan/binary-analysis-tool-bat -b /samples/example.bin -o /samples/example.gz
```

### Or for multiple samples locating in samples directory:
```
docker run -v /samples:/samples cincan/binary-analysis-tool-bat -d /samples -u /samples/output
```

## Optimization:
 - Find out how BAT can be installed on Alpine
