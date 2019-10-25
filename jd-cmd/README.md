# "The jd-cmd is a simple command line wrapper around JD Core Java Decompiler project. Decompiles .dex and .jar -files to java."

## Input

```
.jar -file
```

## Output

```
Folder with java files
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*apk-tools/jd-cli/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/apk-tools/jd-cli/Dockerfile))

## Usage


```
docker run --rm -v `pwd`:/data jdcli -od <Output Folder> <JAR-FILE>
```

## Project homepage

https://github.com/kwart/jd-cmd
