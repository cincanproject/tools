# PDF-parser tool will parse a PDF document to identify it's fundamental elements
ARG tool_version=0_7_4

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache \
	python3 \
	wget \
	unzip \
	git

RUN wget https://didierstevens.com/files/software/pdf-parser_V$TOOL_VERSION.zip \
	&& echo "fc318841952190d51eb70dafb0666d7d19652c8839829cc0c3871bbf7e155b6a  pdf-parser_V$TOOL_VERSION.zip" |sha256sum -c \
	&& unzip pdf-parser_V$TOOL_VERSION.zip -d /pdf-parser \
	&& wget https://github.com/DidierStevens/DidierStevensSuite/archive/master.zip \
	&& unzip master.zip \
	&& cp DidierStevensSuite-master/decoder*py /pdf-parser/ \
	&& rm -rf /DidierStevensSuite-master /pdf-parser_V$TOOL_VERSION.zip /master.zip \
    && apk del --purge wget unzip git

RUN adduser -s /sbin/login -D appuser && ls -la /pdf-parser
USER appuser

WORKDIR /pdf-parser
COPY meta.json /opt/
ENTRYPOINT ["/usr/bin/python3", "pdf-parser.py"]
CMD ["--help"]
