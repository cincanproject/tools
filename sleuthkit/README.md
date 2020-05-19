# "A collection of command line tools that allows you to analyze disk images and recover files."

## Input

```
raw, ewf, vmdk, vhd
```

## Output

```
multiple outputs
```


## Supported tags and respective `Dockerfile` links

* `latest` 
([*sleuthkit/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/sleuthkit/Dockerfile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools.git
cd tools/sleuthkit
```

***2. Build OR pull the docker image***

```
docker build . -t cincan/sleuthkit
docker pull cincan/sleuthkit
```

***3. Run the docker container***  

Example 1. List file system information with `fsstat`  

`$ docker run --rm -v $(pwd):/input cincan/sleuthkit fsstat /input/testdisk.raw`  

Example 2. List files and directories with `fls`  

`$ docker run --rm -v $(pwd):/input cincan/sleuthkit fls /input/testdisk.raw`  

Example 3. Dump all unallocated units of a file system with `blkls` using the CinCan tool:    

`$ cincan run cincan/sleuthkit blkls /input/testdisk.raw`  


## Project homepage

https://www.sleuthkit.org/sleuthkit/

