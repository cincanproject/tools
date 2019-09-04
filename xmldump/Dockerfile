FROM alpine:3.9

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input="text/xml"

COPY commands.json /cincan/commands.json

SHELL ["/bin/sh", "-euxo", "pipefail", "-c"]

RUN apk update && apk add --no-cache \
	py-setuptools=40.6.3-r0 \
	py2-pip=18.1-r0 \
    && wget https://didierstevens.com/files/software/xmldump_V0_0_3.zip \
    && if [ ! "$(sha256sum xmldump_V0_0_3.zip |awk '{print toupper($1)}')" = \
            "C0A3199EA69494962CAC6EC3BA3AD47130BE5BB3D9D7D330579856AC9C314BF0" ]; then \
            echo "Integrity check failed"; exit 1; fi \
    && unzip xmldump_V0_0_3.zip \
    && rm xmldump_V0_0_3.zip \
    && adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["/usr/bin/python","xmldump.py"]
CMD ["--help"]
