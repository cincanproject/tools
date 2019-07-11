FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	py-setuptools=40.6.3-r0 \
	py2-pip=18.1-r0 \
    git=2.20.1-r0 \
    && pip install oletools==0.50	

ADD Oletools-license .

ENTRYPOINT ["olevba"]
CMD ["--help"]
