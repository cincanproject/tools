# "Parse XML files."

## Input

```
XML
```

## Output

```
xmldump report
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*xmldump/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/xmldump/Dockerfile))

## Usage


```
docker run --rm -v /samples:/samples cincan/xmldump /samples/<XML-FILE>
```

***Options***  

```
Usage: xmldump.py [options] command [[@]file ...]
This is essentially a wrapper for xml.etree.ElementTree
Commands:
text wordtext elementtext attributes

Arguments:
@file: process each file listed in the text file specified
wildcards are supported

Source code put in the public domain by Didier Stevens, no Copyright
Use at your own risk
https://DidierStevens.com

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -m, --man             Print manual
  -u, --includeuri      Include URI for the tags
  -o OUTPUT, --output=OUTPUT
                        Output to file
```


## Project homepage

https://blog.didierstevens.com/2018/04/02/update-xmldump-py-version-0-0-3/
