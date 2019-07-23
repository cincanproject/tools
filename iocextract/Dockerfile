FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

RUN apk update \
    && apk add --no-cache alpine-sdk python-dev \
    && pip install iocextract \
    && adduser -s /sbin/login -D appuser

COPY /iocextract .

USER appuser

ENTRYPOINT ["python", "extract.py"]

