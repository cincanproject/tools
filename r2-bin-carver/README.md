# R2 bin carver

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
* `latest` 
([*r2_bin_carver/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/r2_bin_carver/Dockerfile))

## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd dockerfiles/r2_bin_carver/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/r2_bin_carver
docker pull cincan/r2_bin_carver
```

*** Carve a binary from a memory dump ***
```
docker run --rm -v /samples/:/samples cincan/r2_bin_carver /samples/sample.bin 
<OFFSET_TO_CARVE_FROM> <SIZE_OF_BINARY>
```

*** Carve a binary using magic checking and patching ***
```
docker run --rm -v /samples/:/samples cincan/r2_bin_carver -p -b MZ 
/samples/sample.dmp 150720 0x24CC0
```


***Options***  

```
-h, --help   	show this help message and exit  
-b B         	Magic bytes to check for, e.g. MZ  
-p, --patch  	Patch carved PE files```


## Project homepage

https://github.com/countercept/radare2-scripts

