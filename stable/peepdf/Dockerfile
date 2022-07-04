
# docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf

# NOTE, using version number without revisions, which are hard to compare
# This should be ok, since latest update is 4 years ago
ARG tool_version="0.3"

FROM debian:8-slim AS builder
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y \
	python \
	libboost-all-dev \
	autoconf \
	python-pip \
	git \
	pkg-config \
	&& apt-get autoclean \ 
	&& git clone https://github.com/buffer/pyv8.git \
	&& git clone https://github.com/jesparza/peepdf.git

WORKDIR /pyv8
RUN git checkout b5b04074ab901896e310cbc444dd542c06edd58c \
	&& python setup.py build \
	&& python setup.py install

WORKDIR /peepdf
RUN git checkout c74dc65c0ac7e506bae4f2582a2435ec50741f40

FROM debian:10-slim

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /usr/local /usr/local
COPY --from=builder /peepdf /peepdf

RUN apt-get update && apt-get install -y \
	libemu-dev \
	libemu2 \
	python-pip \
	python \
	libboost-all-dev \
	autoconf \
	python-pil \
	jq \
	&& pip install pylibemu \
	&& apt-get autoclean \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
	&& chown -R appuser:appuser /peepdf 

WORKDIR /home/appuser

USER appuser

COPY .cincanignore .

# Copying meta.json should be final modification of layers - fetched separately in some cases
COPY meta.json /opt/

ENTRYPOINT ["/usr/bin/python","/peepdf/peepdf.py"]

