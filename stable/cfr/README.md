# Class File Reader - another java decompiler

Java decompiler by Lee Benfield

## Input

```
.jar -file
```

## Output

```
Folder with java files
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*cfr/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/cfr/Dockerfile))

## Usage

Using the `cincan` command to decompile a `.jar` file to a directory of `.java` source code files:

```
cincan run cincan/cfr --outputdir decompiled sample.jar
```

Using the docker command to achieve the same:

```
docker run --rm -v `pwd`:/data cincan/cfr --outputdir decompiled /data/sample.jar
```

See the generated `summary.txt` for details

## Project homepage

[Project homepage](https://www.benf.org/other/cfr/)
[Project GitHub leibnitz27/cfr](https://github.com/leibnitz27/cfr)
