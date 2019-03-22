# The DidierStevensSuite by Didier Stevens

The DidierStevensSuite from https://github.com/DidierStevens/DidierStevensSuite  

Includes many tools. For example:   
```
pdf-parser.py
pdfid.py
mPDF.py
make-pdf-embedded.py
pecheck.py
base64dump.py
jpegdump.py
oledump.py
```
## Supported tags and respective `Dockerfile` links
* `latest` 
([*pdf-tools/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/pdf-tools/Dockerfile))

## Usage 

***example for pdf-parser.py***

`$ docker run -v /samples:/samples cincan/pdf-tools python pdf-parser.py 
/samples/input/sample.pdf`

***example for base64dump.py***  

`$ docker run -v /samples:/samples cincan/pdf-tools python base64dump.py -e pu -a -s 
1  /samples/input/sample`

## Project homepage

https://github.com/DidierStevens/DidierStevensSuite
