# A Program to analyse OLE files.
ARG tool_version=0_0_50

FROM python:2-slim as builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV HASH=870167ae5576b169eb52572788d04f1ffcec5c8afdebcc59fe3b8b01cbde6cd9

RUN apt-get update && apt-get install -y \
    curl \
	unzip \
	&& curl -OL https://didierstevens.com/files/software/oledump_V$TOOL_VERSION.zip \
	&& echo "$HASH  oledump_V$TOOL_VERSION.zip" | sha256sum -c \
	&& unzip oledump_V$TOOL_VERSION.zip -d /oledump
 

FROM python:2-slim

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /oledump /oledump

RUN pip install olefile==0.46 && \
    groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /sbin/nologin appuser

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["/usr/local/bin/python","/oledump/oledump.py"]
CMD ["--help"]
