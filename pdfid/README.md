# Scan PDF's for certain keywords, Javascript, auto-open functions etc.

## Input

```
PDF
```

## Output

```
PDFiD report
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*pdfid/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/pdfid/Dockerfile))


## Usage

***EXAMPLE 1***

```
docker run --rm -v /samples:/samples cincan/pdfid /samples/sample.pdf
```

***EXAMPLE 2***

```
docker run --rm -v $(pwd):/samples cincan/pdfid /samples/sample.pdf -p plugin_triage
```


***Options***
```  

--version             : show program's version number and exit

-h, --help            : show this help message and exit

-s, --scan            : scan the given directory

-a, --all             : display all the names

-e, --extra           : display extra data, like dates

-f, --force           : force the scan of the file, even without proper %PDF header
                        
-d, --disarm          :  disable JavaScript and auto launch

-p PLUGINS, --plugins=PLUGINS
                      : plugins to load (separate plugins with a comma , ; @file supported)
                      
-c, --csv             : output csv data when using plugins

-m MINIMUMSCORE, --minimumscore=MINIMUMSCORE
                      : minimum score for plugin results output
                  
-v, --verbose         : verbose (will also raise catched exceptions)

-S SELECT, --select=SELECT
                      : selection expression
                      
-n, --nozero          : supress output for counts equal to zero

-o OUTPUT, --output=OUTPUT
                      : output to log file
                    
--pluginoptions=PLUGINOPTIONS
                      : options for the plugin
                
-l, --literalfilenames: take filenames literally, no wildcard matching
                
--recursedir          : Recurse directories (wildcards and here files (@...) allowed)
```

## Project homepage

[https://blog.didierstevens.com/programs/pdf-tools/#pdfid](https://blog.didierstevens.com/programs/pdf-tools/#pdfid)
