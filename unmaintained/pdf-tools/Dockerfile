# "The DidierStevensSuite from https://github.com/DidierStevens/DidierStevensSuite"
#
# Includes many tools. For example: 
# pdf-parser.py, pdfid.py, mPDF.py, make-pdf-embedded.py, 
# pecheck.py, base64dump.py, jpegdump.py, oledump.py
#
# 
# build:
# docker build -t cincan/pdf-tools .
#
# usage example for pdf-parser.py:
# docker run -v /samples:/samples cincan/pdf-tools python pdf-parser.py /samples/input/sample.pdf
#
# example for base64dump.py:
# docker run -v /samples:/samples cincan/pdf-tools python base64dump.py -e pu -a -s 1  /samples/input/sample

FROM alpine:3.10

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	    python \
	    git  \
	    py-pip \
    && git clone https://github.com/DidierStevens/DidierStevensSuite.git \
	&& pip install pefile \
    && adduser -s /sbin/login -D appuser

USER appuser

WORKDIR /DidierStevensSuite

CMD echo "See all commands: https://github.com/DidierStevens/DidierStevensSuite"

