FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	python3=3.7.5-r1 \
	musl-dev=1.1.22-r3 \
	gcc=8.3.0-r0 \
	&& pip3 install requests==2.22.0 \
	   ioc_strings==0.1.4 \
	&& adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["iocstrings", "-t"]

