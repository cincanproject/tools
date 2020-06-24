# Command line wrapper around JD Core Java Decompiler. Decompiles .dex and .jar -files to java.

## Input

```
.jar -file
```

## Output

```
Folder with java files
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*jd-cmd/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/jd-cmd/Dockerfile))

## Usage

Using the `cincan` command to decompile a `.jar` file to a decompiled `.jar` file:

```
cincan run jd-cmd -od decompiled sample.jar
```

Using the docker command to achieve the same:

```
docker run --rm -v `pwd`:/data jdcli -od decompiled sample.jar
```

## Project homepage

https://github.com/kwart/jd-cmd
