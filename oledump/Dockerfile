# A Program to analyse OLE files.
ARG tool_version=0_0_48

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV HASH=0e66e3ea42d5761301e0643a27d892b3c4531ccc2e4c95373ece9b7ad7e6dac6

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	py-setuptools \
	py2-pip \
	jq \
	git \
	unzip \
	&& wget https://didierstevens.com/files/software/oledump_V$TOOL_VERSION.zip \
	&& echo "$HASH  oledump_V$TOOL_VERSION.zip" | sha256sum -c \
	&& unzip oledump_V$TOOL_VERSION.zip -d /oledump \
	&& rm oledump_V$TOOL_VERSION.zip \
	&& pip install olefile==0.46 \
	&& adduser -s /sbin/login -D appuser \
	&& chown -R appuser:appuser /oledump
 
USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["/usr/bin/python","/oledump/oledump.py"]
CMD ["--help"]
