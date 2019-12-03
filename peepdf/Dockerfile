
# docker run -v /samples:/samples cincan/peepdf /samples/sample.pdf

FROM debian:8-slim AS builder

LABEL MAINTAINER=cincan.io

ENV VERSION="0.3 r275"

RUN apt-get update && apt-get install -y \
	python=2.7.9-1 \
	libboost1.55-all-dev=1.55.0+dfsg-3 \
	autoconf=2.69-8 \
	python-pip=1.5.6-5 \
	git=1:2.1.4-2.1+deb8u7 \
	pkg-config=0.28-1 \
	jq=1.4-2.1+deb8u1 \
	&& apt-get autoclean \ 
	&& git clone https://github.com/buffer/pyv8.git \
	&& git clone https://github.com/jesparza/peepdf.git

WORKDIR /pyv8
RUN git checkout b5b04074ab901896e310cbc444dd542c06edd58c \
	&& python setup.py build \
	&& python setup.py install

WORKDIR /peepdf
RUN git checkout c74dc65c0ac7e506bae4f2582a2435ec50741f40


FROM debian:8-slim

COPY --from=builder /usr/local /usr/local
COPY --from=builder /peepdf /peepdf

RUN apt-get update && apt-get install -y \
	libemu-dev=0.2.0+git20120122-1.2 \
	libemu2=0.2.0+git20120122-1.2 \
	python-pip=1.5.6-5 \
	python=2.7.9-1 \
	libboost1.55-all-dev=1.55.0+dfsg-3 \
	autoconf=2.69-8 \
	python-pil=2.6.1-2+deb8u3  \
	&& pip install pylibemu==0.5.8 \
	&& apt-get autoclean \
	&& adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
	&& chown -R appuser:appuser /peepdf 

WORKDIR /home/appuser

USER appuser

ENTRYPOINT ["/usr/bin/python","/peepdf/peepdf.py"]

