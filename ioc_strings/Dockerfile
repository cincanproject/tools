FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

RUN apt update \
    && apt install python3 python3-pip \
    && pip3 install ioc_strings

ENTRYPOINT ["iocstrings", "-t"]