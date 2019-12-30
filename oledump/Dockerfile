# A Program to analyse OLE files.

FROM alpine:3.9

LABEL MAINTAINER=cincan.io

ENV VERSION=0_0_44

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	py-setuptools=40.6.3-r0 \
	py2-pip=18.1-r0 \
	jq=1.6-r0 \
	git=2.20.2-r0 \
	unzip=6.0-r4 \
	&& wget https://didierstevens.com/files/software/oledump_V$VERSION.zip \
	&& echo "1a9c951e95e2fe0fdf3a3dc8e331205bc65c617953f0e30ed3e6ac045f4dd0c0  oledump_V$VERSION.zip" | sha256sum -c \
	&& unzip oledump_V$VERSION.zip -d /oledump \
	&& rm oledump_V$VERSION.zip \
	&& pip install olefile==0.46 \
	&& adduser -s /sbin/login -D appuser \
	&& chown -R appuser:appuser /oledump
 
USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["/usr/bin/python","/oledump/oledump.py"]
CMD ["--help"]
