# PDF-parser tool will parse a PDF document to identify it's fundamental elements

FROM alpine:3.5

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input="application/pdf"

ENV VERSION=0_7_3

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	python3=3.5.6-r0 \
	wget=1.18-r4 \
	unzip=6.0-r3 \
	git=2.11.3-r2

RUN wget https://didierstevens.com/files/software/pdf-parser_V$VERSION.zip \
	&& if [ ! "$(sha256sum pdf-parser_V$VERSION.zip |awk '{print toupper($1)}')" = \
	"D4D5AC9C26A9D8FEF65CE58A769D3F64A737860DC26606068CCDD3F04FDEA0D7" ]; then \
	echo "Integrity check failed"; exit 1; fi \
	&& unzip pdf-parser_V$VERSION.zip -d /pdf-parser \
	&& wget https://github.com/DidierStevens/DidierStevensSuite/archive/master.zip \
	&& unzip master.zip \
	&& cp DidierStevensSuite-master/decoder*py /pdf-parser/ \
	&& rm -rf /DidierStevensSuite-master /pdf-parser_V$VERSION.zip /master.zip 

RUN adduser -s /sbin/login -D appuser && ls -la /pdf-parser
USER appuser

WORKDIR /pdf-parser

ENTRYPOINT ["/usr/bin/python3", "pdf-parser.py"]
CMD ["--help"]
