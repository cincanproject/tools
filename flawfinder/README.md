# Flawfinder
a simple program that examines C/C++ source code and reports possible security weaknesses (“flaws”) sorted by risk level

## Build:
```
docker build -t cincan/flawfinder .
```

## Usage:
```
docker run -v /samples:/samples cincan/flawfinder /samples/sample.c
```
