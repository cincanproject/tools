# "PDF-parser tool will parse a PDF document to identify the fundamental
#  elements used in the analyzed file"

FROM alpine:3.9

LABEL MAINTAINER=cincan.io
LABEL io.cincan.input="application/pdf"

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	python2=2.7.16-r1 \
	wget=1.20.3-r0 \
	unzip=6.0-r4 \
	git=2.20.1-r0

RUN wget https://didierstevens.com/files/software/pdf-parser_V0_7_3.zip \
	&& if [ ! "$(sha256sum pdf-parser_V0_7_3.zip |awk '{print toupper($1)}')" = \
	"D4D5AC9C26A9D8FEF65CE58A769D3F64A737860DC26606068CCDD3F04FDEA0D7" ]; then \
	echo "Integrity check failed"; exit 1; fi \
	&& unzip pdf-parser_V0_7_3.zip -d /pdf-parser \
	&& wget https://github.com/DidierStevens/DidierStevensSuite/archive/master.zip \
	&& unzip master.zip \
	&& cp DidierStevensSuite-master/decoder*py /pdf-parser/ \
	&& rm -rf /DidierStevensSuite-master /pdf-parser_V0_7_3.zip /master.zip 

RUN adduser -s /sbin/login -D appuser && ls -la /pdf-parser
USER appuser

WORKDIR /pdf-parser

ENTRYPOINT ["/usr/bin/python", "pdf-parser.py"]
CMD ["--help"]
