#"PDFID will scan a file to look for certain PDF keywords, allowing you to 
# identify PDF documents that contain (for example) JavaScript or execute 
# an action when opened. PDFiD will also handle name obfuscation."
ARG tool_version=0_2_8

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV HASH=0d0aa12592fa29bc5e7a9c3cfa0aaebb711cef373a0ae0ad523723c64c9d02b4

RUN apk update && apk add --no-cache \
	python2 \
	wget \
	unzip \
	git \
	jq

# Get pdfid, check integrity, unzip, clean up.
# Replace main script of pdfid with one supporting JSON output
RUN wget https://didierstevens.com/files/software/pdfid_v$TOOL_VERSION.zip \
	&& if [ ! "$(sha256sum pdfid_v$TOOL_VERSION.zip |awk '{print tolower($1)}')" = "$HASH" ]; then \
	echo "Integrity check failed"; exit 1; fi \
	&& unzip pdfid_v$TOOL_VERSION.zip -d /pdfid \
	&& rm pdfid_v$TOOL_VERSION.zip 

RUN adduser -s /sbin/login -D appuser

USER appuser
WORKDIR /home/appuser
COPY meta.json /opt/
ENTRYPOINT ["/usr/bin/python", "/pdfid/pdfid.py"]
CMD ["--help"]
