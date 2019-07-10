#"PDFID will scan a file to look for certain PDF keywords, allowing you to 
# identify PDF documents that contain (for example) JavaScript or execute 
# an action when opened. PDFiD will also handle name obfuscation."

FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
	python2=2.7.16-r1 \
	wget=1.20.3-r0 \
	unzip=6.0-r4 \
	git=2.20.1-r0

# Get pdfid, check integrity, unzip, clean up.
# Replace main script of pdfid with one supporting JSON output
RUN wget https://didierstevens.com/files/software/pdfid_v0_2_5.zip \
	&& if [ ! "$(sha256sum pdfid_v0_2_5.zip |awk '{print toupper($1)}')" = \
	"4DD43D7BDA885C5A579FC1F797E93A536E1DB5A4AB52A9337759A69D3B0250E0" ]; then \
	echo "Integrity check failed"; exit 1; fi \
	&& unzip pdfid_v0_2_5.zip -d /pdfid \
	&& rm pdfid_v0_2_5.zip && \
	rm pdfid/pdfid.py && \
	wget https://raw.githubusercontent.com/Nicceboy/DidierStevensSuite/master/pdfid.py -P pdfid \
	&& if [ ! "$(sha256sum pdfid/pdfid.py |awk '{print toupper($1)}')" = \
	"FF80CCE6063BB7D9B4FA5474F469AC57EED86BA18B9AF21FF3536ABD73C4CA37" ]; then \
	echo "Integrity check failed"; exit 1; fi

ENTRYPOINT ["/usr/bin/python", "pdfid/pdfid.py"]
CMD ["--help"]
