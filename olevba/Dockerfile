FROM alpine:3.9

# olevba latest installation in python3

LABEL MAINTAINER=cincan.io

RUN apk update && \
	apk add --no-cache --update python3 \
	python3-dev \
	openssl-dev \
	git=2.20.1-r0 \ 
	gcc \
	libffi-dev \
	libc-dev && \
	pip3 install --upgrade pip && \
	pip3 install --upgrade pip setuptools 

RUN pip3 install -U oletools

RUN apk del openssl-dev \
	gcc \
	libffi-dev \
	python3-dev \
	libc-dev

ADD Oletools-license .

ENTRYPOINT ["olevba"]
# CMD ["--help"]
