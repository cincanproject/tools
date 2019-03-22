# Powerful Python tool to analyze PDF documents.

## Input

```
PDF
```

## Output

```
Peepdf report (XML, JSON)
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*peepdf/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/peepdf/Dockerfile))


## Usage


***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/dockerfiles
cd dockerfiles/peepdf/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/peepdf
docker pull cincan/peepdf
```

***3. Run the docker container***

```
docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf -f
```

***Interactive mode***
```
docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf -f -i
```


***Options***
```  

-h, --help            : show this help message and exit

-i, --interactive     : Sets console mode.

-s SCRIPTFILE, --load-script=SCRIPTFILE
                      : Loads the commands stored in the specified file and
                        execute them.
                        
-c, --check-vt        : Checks the hash of the PDF file on VirusTotal.

-f, --force-mode      : Sets force parsing mode to ignore errors.

-l, --loose-mode      : Sets loose parsing mode to catch malformed objects.

-m, --manual-analysis : Avoids automatic Javascript analysis. Useful with
                        eternal loops like heap spraying.
                        
-u, --update          : Updates peepdf with the latest files from the
                        repository.
                        
-g, --grinch-mode     : Avoids colorized output in the interactive console.

-v, --version         : Shows program's version number.

-x, --xml             : Shows the document information in XML format.

-j, --json            : Shows the document information in JSON format.

-C COMMANDS, --command=COMMANDS
                      : Specifies a command from the interactive console to be
                        executed.
```

## Project homepage

[https://github.com/jesparza/peepdf](https://github.com/jesparza/peepdf)
