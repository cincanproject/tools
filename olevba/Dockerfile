FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	    py-setuptools=40.6.3-r0 \
	    py2-pip=18.1-r0 \
    git=2.20.1-r0 \
    && pip install oletools==0.50 \
    && adduser -s /sbin/login -D appuser

ADD Oletools-license .

USER appuser

ENTRYPOINT ["olevba"]
CMD ["--help"]
