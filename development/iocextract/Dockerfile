FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	alpine-sdk=1.0-r0 \
	python-dev=2.7.16-r1 \
    && pip install iocextract==1.13.1 \
    && adduser -s /sbin/login -D appuser

COPY /iocextract .

USER appuser

ENTRYPOINT ["python", "extract.py"]

