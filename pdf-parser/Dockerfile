# PDF-parser tool will parse a PDF document to identify it's fundamental elements

FROM alpine:3.5

LABEL MAINTAINER=cincan.io

ENV VERSION=0_7_4

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	python3=3.5.6-r0 \
	wget=1.18-r4 \
	unzip=6.0-r3 \
	git=2.11.3-r2

RUN wget https://didierstevens.com/files/software/pdf-parser_V$VERSION.zip \
	&& echo "fc318841952190d51eb70dafb0666d7d19652c8839829cc0c3871bbf7e155b6a  pdf-parser_V$VERSION.zip" |sha256sum -c \
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
