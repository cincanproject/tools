# Convert shellcodes into executable files, for multiple platforms.

## Input

```
shellcode
```

## Output

```
ELF / PE
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*shellcode2exe/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/shellcode2exe/Dockerfile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/dockerfiles
cd dockerfiles/shellcode2exe/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/shellcode2exe
docker pull cincan/shellcode2exe
```

***3. Run the docker container***

Shellcode file "shellcode.file" in folder "/samples" :  

`$ docker run --rm -v /samples:/samples cincan/shellcode2exe /samples/shellcode.file`  

Shellcode file "shellcode.file" of unicode format is in current folder, outputs linux 
ELF binary for i386 architecture:  

`$ docker run --rm -v $(pwd):/samples cincan/shellcode2exe /samples/shellcode.file -u 
--arch=i386 --os=linux`  

***Options***
```
-h, --help            : show this help message and exit  

-a ARCH, --arch=ARCH  : target architecture [i386(default)|powerpc|sparc|arm]  

-o OS, --os=OS        : target operating system [windows(default)|linux|freebsd|openbsd|solaris]

-c, --asciicmd        : enable ascii entry in command line (e.g. -c '\x90\x90')  

-s, --asciifile       : enable ascii entry in input file  

-d, --unicodecmd      : enable unicode entry in command line (e.g. -d '%u9090')  

-u, --unicodefile     : enable unicode entry in input file  

```

## Project homepage

[https://github.com/MarioVilas/shellcode_tools](https://github.com/MarioVilas/shellcode_tools)
