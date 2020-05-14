ARG tool_version=0.1.5

FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
	python3>3.7.5 \
	musl-dev>1.1.22 \
	gcc>8.3.0 \
	&& pip3 install requests==2.22.0 \
	   ioc_strings==${TOOL_VERSION} \
	&& adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["iocstrings", "-t"]

