# A Program to analyse OLE files.

FROM alpine:3.9

LABEL MAINTAINER=cincan.io

ENV VERSION=0_0_42

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	py-setuptools=40.6.3-r0 \
	py2-pip=18.1-r0 \
	jq=1.6-r0 \
	git=2.20.2-r0 \
	unzip=6.0-r4 \
	&& wget https://didierstevens.com/files/software/oledump_V$VERSION.zip \
	&& if [ ! "$(sha256sum oledump_V$VERSION.zip |awk '{print toupper($1)}')" = \
		"14A1FDA4AB57B09729AEB2697818782FAE498369A760FEC8AEE5CFB0A0E9D126" ]; then \
		echo "Integrity check failed"; exit 1; fi \
	&& unzip oledump_V$VERSION.zip -d /oledump \
	&& rm oledump_V$VERSION.zip \
	&& pip install olefile==0.46 \
	&& adduser -s /sbin/login -D appuser \
	&& chown -R appuser:appuser /oledump
 
USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["/usr/bin/python","/oledump/oledump.py"]
CMD ["--help"]
