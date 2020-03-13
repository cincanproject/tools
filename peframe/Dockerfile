FROM alpine:latest

LABEL MAINTAINER=cincan.io

# Commit after 6.0.3 release
ENV VERSION=f7d75aa2b2d39ef76e928808598d53e922bdeae5

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
	&& git checkout "${VERSION}" \
	&& chmod +x install.sh \
	&& sh install.sh \
	&& python3 setup.py install \
	&& adduser --shell /sbin/login --gecos "" appuser -DH

USER appuser

WORKDIR /home/appuser/peframe

ENTRYPOINT ["peframe"]
CMD ["-h"]
