#build:
#docker build -t cincan/pdfxray_lite .
#
#usage for one file, write results to a report file:
#docker run -v /samples:/samples cincan/pdfxray_lite -f /samples/input/sample.pdf -r /samples/output/report
#
#analyze all files in a directory:
#docker run -v /samples:/samples cincan/pdfxray_lite -d /samples/input/ -r /samples/output/report

FROM alpine:3.10

RUN apk update && apk add --no-cache \
	    git \
	    python \
	    py-simplejson \
    && git clone https://github.com/9b/pdfxray_lite.git \
    && adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["/usr/bin/python","pdfxray_lite/pdfxray_lite.py"]

