# A Program to analyse OLE files.
ARG tool_version=0_0_55

FROM python:2-slim as builder

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV HASH=abeabff0f1f5aa2239afcde73a676d4e8d9ba2f82c03b8663ffab6f8d3a360e7

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

ENTRYPOINT ["/usr/local/bin/python","/oledump/oledump.py"]
CMD ["--help"]
