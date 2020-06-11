# "Flawfinder - Finds possible security weaknesses in C/C++ source code"

## Supported tags and respective `Dockerfile` links
* `latest` 
([*flawfinder/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/flawfinder/Dockerfile))

### Input  

```
C/C++ code
```

### Output

```
Flawfinder report
```

## Usage

`$ cincan run cincan/flawfinder sample.c`

`$ docker run -v /samples:/samples cincan/flawfinder /samples/sample.c`

## Project homepage

https://github.com/david-a-wheeler/flawfinder
