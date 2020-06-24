ARG tool_version="1.13.1"

FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV ALPINE_SDK_VERSION 1.0-r0
ENV PYTHON_DEV_VERSION 3.8.3-r0

RUN apk update && apk add --no-cache \
	alpine-sdk=$ALPINE_SDK_VERSION \
	python3-dev=$PYTHON_DEV_VERSION \
    && pip install iocextract==$TOOL_VERSION \
    && adduser -s /sbin/login -D appuser

WORKDIR /home/appuser

COPY /iocextract .

USER appuser

ENTRYPOINT ["python", "extract.py"]

