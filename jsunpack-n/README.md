# Emulates browser functionality when visiting an URL. Detects browser exploits, scans PDF.

## Input

```
PDF, URL, PCAP, JavaSCript, SWF
```

## Output

```
jsunpack-n report
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*jsunpack-n/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/jsunpack-n/Dockerfile))


## Usage

***FILE SCAN***

```
docker run -v /samples:/samples cincan/jsunpack-n /samples/input/sample.pdf -d /samples/output
```

***URL SCAN***

```
docker run -v /samples:/samples cincan/jsunpack-n -u https://<TARGET.URL> -d /samples/output -V
```

 
***Options***  

```  
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout=TIMEOUT
                        limit on number of seconds to evaluate JavaScript
  -r REDOEVALTIME, --redoEvalLimit=REDOEVALTIME
                        maximium evaluation time to allow processing of
                        alternative version strings
  -m MAXRUNTIME, --maxRunTime=MAXRUNTIME
                        maximum running time (seconds; cumulative total). If
                        exceeded, raise an alert (default: no limit)
  -f, --fast-evaluation
                        disables (multiversion HTML,shellcode XOR) to improve
                        performance
  -u URLFETCH, --urlFetch=URLFETCH
                        actively fetch specified URL (for fully active fetch
                        use with -a)
  -d OUTDIR, --destination-directory=OUTDIR
                        output directory for all suspicious/malicious content
  -c CONFIGFILE, --config=CONFIGFILE
                        configuration filepath (default options.config)
  -s, --save-all        save ALL original streams/files in output dir
  -e, --save-exes       save ALL executable files in output dir
  -a, --active          actively fetch URLs (only for use with pcap/file/url
                        as input)
  -p PROXY, --proxy=PROXY
                        use a random proxy from this list (comma separated)
  -P CURRENTPROXY, --currentproxy=CURRENTPROXY
                        use this proxy and ignore proxy list from --proxy
  -q, --quiet           limited output to stdout
  -v, --verbose         verbose mode displays status for all files and
                        decoding stages, without this option reports only
                        detection
  -V, --very-verbose    shows all decoding errors (noisy)
  -g GRAPHFILE, --graph-urlfile=GRAPHFILE
                        filename for URL relationship graph, 60 URLs maximium
                        due to library limitations
  -i INTERFACE, --interface=INTERFACE
                        live capture mode, use at your own risk (example eth0)
  -D, --debug           (experimental) debugging option, do not delete
                        temporary files
  -J, --javascript-decode-disable
                        (experimental) dont decode anything, if you want to
                        just use the original contents

```


## Project homepage

[https://github.com/urule99/jsunpack-n](https://github.com/urule99/jsunpack-n)
