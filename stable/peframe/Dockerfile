FROM python:3.8-alpine
# Latest alpine with python 3.8

LABEL MAINTAINER=cincan.io

# Commit after 6.0.3 release
# Python version 3.6 <= ver < 3.9
ARG tool_version=70683b6db71c7a1c44c2d8f817822a0815fc6137
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
	git \
	libssl1.1 \
	python3 \
    py3-pip \
	swig \
	g++ \
	make \
	openssl-dev \
	python3-dev \
    py3-setuptools \
	libffi-dev \
	libmagic \
    rust \
    cargo \
	&& git clone https://github.com/guelfoweb/peframe.git \
	&& cd peframe \
	&& git checkout "${TOOL_VERSION}" \
	&& chmod +x install.sh \
    && pip install setuptools-rust wheel \
	&& sh install.sh \
	&& python3 setup.py install \
	&& adduser --shell /sbin/login --gecos "" appuser -DH

USER appuser

WORKDIR /home/appuser/peframe

# Should be final modification for layers - fetched separately
COPY meta.json /opt/

ENTRYPOINT ["peframe"]
CMD ["-h"]
