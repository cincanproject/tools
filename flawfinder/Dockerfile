FROM alpine:3.10

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache python3=3.7.3-r0 \
    && pip3 install flawfinder==2.0.10 \
    && adduser -s /sbin/nologin -D appuser

USER appuser
ENTRYPOINT ["flawfinder"]
