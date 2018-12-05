# CERT Keyfinder
finding and analyzing key files on a filesystem and within Android APK files.

## Build:
```
docker build -t cincan/keyfinder .
```

## Usage:
```
docker run -v /samples:/samples cincan/keyfinder -v -k /samples
```
