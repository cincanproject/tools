## Keyfinder

### "Finding and analyzing key files on a filesystem and within Android APK files"

## Supported tags and respective `Dockerfile` links
* `latest` 
([*keyfinder/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/keyfinder/Dockerfile))

### Input

```
filesystem, APK
```

### Output

```
Keyfinder report
```

## Usage

`$ docker run -v /samples:/samples cincan/keyfinder -v -k /samples`

## Project homepage

https://github.com/CERTCC/keyfinder
