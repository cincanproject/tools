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

## Docker Compose file (Optional)

```yml
---
```

## Usage

***EXAMPLE 1***

```
docker run --rm -v /samples:/samples shellcode2exe /samples/shellcode
```

***EXAMPLE 2***

```
docker run --rm -v $(pwd):/samples shellcode2exe /samples/shellcode -u --arch=i386 --os=linux
```


***Options***
```
-h, --help            : show this help message and exit  

-a ARCH, --arch=ARCH  : target architecture [default: i386]  

-o OS, --os=OS        : target operating system [default: windows]

-c, --asciicmd        : enable ascii entry in command line (e.g. -c
                        '\x90\x90')  

-s, --asciifile       : enable ascii entry in input file  

-d, --unicodecmd      : enable unicode entry in command line (e.g. -d  

                        '%u9090')  

-u, --unicodefile     : enable unicode entry in input file  


```

## Project homepage

[https://github.com/MarioVilas/shellcode_tools/blob/master/shellcode2exe.py](https://github.com/MarioVilas/shellcode_tools/blob/master/shellcode2exe.py)
