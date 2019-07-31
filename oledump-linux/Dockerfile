FROM alpine:3.9

LABEL MAINTAINER=cincan.io

SHELL ["/bin/sh", "-euxo", "pipefail", "-c"]

RUN apk update && apk add --no-cache \
	    py-setuptools=40.6.3-r0 \
	    py2-pip=18.1-r0 \
	git=2.20.1-r0 \
    && wget https://didierstevens.com/files/software/oledump_V0_0_42.zip \
    && if [ ! "$(sha256sum oledump_V0_0_42.zip |awk '{print toupper($1)}')" = \
            "14A1FDA4AB57B09729AEB2697818782FAE498369A760FEC8AEE5CFB0A0E9D126" ]; then \
            echo "Integrity check failed"; exit 1; fi \
    && unzip oledump_V0_0_42.zip \
    && rm oledump_V0_0_42.zip \
    && pip install olefile==0.46 \
    && adduser -s /sbin/login -D appuser

#USER appuser

ENTRYPOINT ["/usr/bin/python","oledump.py"]
CMD ["--help"]
