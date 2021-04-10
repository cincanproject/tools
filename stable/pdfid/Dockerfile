#"PDFID will scan a file to look for certain PDF keywords, allowing you to 
# identify PDF documents that contain (for example) JavaScript or execute 
# an action when opened. PDFiD will also handle name obfuscation."
ARG tool_version=0_2_7

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV HASH=FE2B59FE458ECBC1F91A40095FB1536E036BDD4B7B480907AC4E387D9ADB6E60

RUN apk update && apk add --no-cache \
	python2 \
	wget \
	unzip \
	git \
	jq

# Get pdfid, check integrity, unzip, clean up.
# Replace main script of pdfid with one supporting JSON output
RUN wget https://didierstevens.com/files/software/pdfid_v$TOOL_VERSION.zip \
	&& if [ ! "$(sha256sum pdfid_v$TOOL_VERSION.zip |awk '{print toupper($1)}')" = "$HASH" ]; then \
	echo "Integrity check failed"; exit 1; fi \
	&& unzip pdfid_v$TOOL_VERSION.zip -d /pdfid \
	&& rm pdfid_v$TOOL_VERSION.zip && \
	rm pdfid/pdfid.py && \
	wget https://raw.githubusercontent.com/Nicceboy/DidierStevensSuite/master/pdfid.py -P pdfid \
	&& if [ ! "$(sha256sum pdfid/pdfid.py |awk '{print toupper($1)}')" = \
	"8D70E711929079B3B3BD64C957AA78C86202DAEB6510851D6FDEEE387ED32CA1" ]; then \
	echo "Integrity check failed"; exit 1; fi

RUN adduser -s /sbin/login -D appuser

USER appuser
WORKDIR /home/appuser
COPY meta.json /opt/
ENTRYPOINT ["/usr/bin/python", "/pdfid/pdfid.py"]
CMD ["--help"]
