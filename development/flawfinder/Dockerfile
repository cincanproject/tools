FROM alpine:latest

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache python3 py3-pip \
    && pip3 install flawfinder==2.0.10 \
    && adduser -s /sbin/nologin -D appuser

USER appuser
ENTRYPOINT ["flawfinder"]
