ARG tool_version=2.0.11
FROM alpine:3.10
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk add --update --no-cache py3-pip
ENV FLAWFINDER_SHA256 af7ec17dc2c0efcb3511931007c418802fcf7f29bc8b732ffbeca58a579cacef
RUN pip3 download flawfinder==2.0.11 &&\
    echo "$FLAWFINDER_SHA256 flawfinder-2.0.11-py2.py3-none-any.whl" | sha256sum -c

RUN apk update && apk add --no-cache python3=3.7.4-r0 \
    && pip3 install flawfinder==2.0.11 \
    && adduser -s /sbin/nologin -D appuser

USER appuser
ENTRYPOINT ["flawfinder"]
