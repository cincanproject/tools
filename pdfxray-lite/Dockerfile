#build:
#docker build -t cincan/pdfxray-lite .
#
#usage for one file, write results to a report file:
#docker run -v /samples:/samples cincan/pdfxray-lite -f /samples/input/sample.pdf -r /samples/output/report
#
#analyze all files in a directory:
#docker run -v /samples:/samples cincan/pdfxray-lite -d /samples/input/ -r /samples/output/report

ARG tool_version=1.0

FROM alpine:latest
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
	    git \
	    python3 \
	    py-simplejson \
    && git clone https://github.com/9b/pdfxray_lite.git \
    && adduser -s /sbin/login -D appuser

WORKDIR /home/appuser

USER appuser

ENTRYPOINT ["/usr/bin/python","/pdfxray_lite/pdfxray_lite.py"]

