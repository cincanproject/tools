FROM alpine:3.10.3

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	git=2.22.0-r0 \
	libssl1.1=1.1.1d-r0 \
	python3=3.7.5-r1 \
	swig=3.0.12-r4 \
	g++=8.3.0-r0 \
	make=4.2.1-r2 \
	openssl-dev=1.1.1d-r0 \
	python3-dev=3.7.5-r1 \
	libffi-dev=3.2.1-r6 \
	libmagic=5.37-r1 \
	&& git clone https://github.com/guelfoweb/peframe.git \
	&& cd peframe \
	&& chmod +x install.sh \
	&& sh install.sh \
	&& python3 setup.py install \
	&& adduser --shell /sbin/login --gecos "" appuser -DH \
	&& chown -R appuser:appuser /peframe

USER appuser

WORKDIR /peframe

ENTRYPOINT ["peframe","-j"]
CMD ["-h"]
