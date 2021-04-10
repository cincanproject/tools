# A Program to analyse OLE files.
ARG tool_version=0_0_60

FROM python:2-slim as builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV HASH=d847e499cb84b034e08bcddc61addada39b90a5fa2e1aba0756a05039c0d8ba2

RUN apt-get update && apt-get install -y \
    curl \
	unzip \
	&& curl -OL https://didierstevens.com/files/software/oledump_V$TOOL_VERSION.zip \
	&& echo "$HASH  oledump_V$TOOL_VERSION.zip" | sha256sum -c \
	&& unzip oledump_V$TOOL_VERSION.zip -d /oledump
 

FROM python:2-alpine

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /oledump /oledump

RUN pip install olefile==0.46 && \
    addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

USER appuser

WORKDIR /home/appuser

COPY meta.json /opt/

ENTRYPOINT ["/usr/local/bin/python","/oledump/oledump.py"]
CMD ["--help"]
