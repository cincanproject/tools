FROM python:3.5-alpine

LABEL MAINTAINER=cincan.io

RUN apk add --no-cache jq \
    && pip install --upgrade pip \
    && pip install --upgrade awscli \
    && adduser -s /sbin/login -D appuser


ADD assets/ /opt/resource/

USER appuser
