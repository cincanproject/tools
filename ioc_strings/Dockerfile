FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
    python3 py3-pip musl-dev gcc \
    && pip3 install requests ioc_strings

ENTRYPOINT ["iocstrings", "-t"]
