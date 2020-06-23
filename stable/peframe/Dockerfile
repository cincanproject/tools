# Commit after 6.0.3 release
ARG tool_version=f7d75aa2b2d39ef76e928808598d53e922bdeae5

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
	git \
	libssl1.1 \
	python3 \
	swig \
	g++ \
	make \
	openssl-dev \
	python3-dev \
	libffi-dev \
	libmagic \
	&& git clone https://github.com/guelfoweb/peframe.git \
	&& cd peframe \
	&& git checkout "${TOOL_VERSION}" \
	&& chmod +x install.sh \
	&& sh install.sh \
	&& python3 setup.py install \
	&& adduser --shell /sbin/login --gecos "" appuser -DH

USER appuser

WORKDIR /home/appuser/peframe

ENTRYPOINT ["peframe"]
CMD ["-h"]
