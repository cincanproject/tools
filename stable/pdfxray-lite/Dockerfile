#build:
#docker build -t cincan/pdfxray-lite .
#
#usage for one file, write results to a report file:
#docker run -v /samples:/samples cincan/pdfxray-lite -f /samples/input/sample.pdf -r /samples/output/report
#
#analyze all files in a directory:
#docker run -v /samples:/samples cincan/pdfxray-lite -d /samples/input/ -r /samples/output/report

ARG tool_version=751377faeb0d2178dcf00dd3f80652f16e04b019

# On later versions of Alpine, no all python2 modules
FROM alpine:3.11
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache \
	    git \
	    python2 \
	    py2-simplejson \
    && git clone https://github.com/9b/pdfxray_lite.git \
    && cd pdfxray_lite && git checkout "$TOOL_VERSION" \
    && adduser -s /sbin/login -D appuser

WORKDIR /home/appuser

USER appuser
COPY meta.json /opt/
ENTRYPOINT ["/usr/bin/python","/pdfxray_lite/pdfxray_lite.py"]

