# " A script used to carve files from memory dumps."

## Input

```
memory dumps
```

## Output

```
binary
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*r2_bin_carver/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/r2_bin_carver/Dockerfile))

## Usage


*** Carve a binary from a memory dump ***
```
docker run --rm -v /samples/:/samples cincan/r2_bin_carver /samples/sample.bin <OFFSET_TO_CARVE_FROM> <SIZE_OF_BINARY>
```

*** Carve a binary using magic checking and patching ***
```
docker run --rm -v /samples/:/samples cincan/r2_bin_carver -p -b MZ /samples/sample.dmp 150720 0x24CC0
```


***Options***  

```
-h, --help   	show this help message and exit
-b B         	Magic bytes to check for, e.g. MZ
-p, --patch  	Patch carved PE files```


## Project homepage

https://github.com/countercept/radare2-scripts
