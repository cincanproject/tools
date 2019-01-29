#build:
#docker build -t cincan/pdfxray_lite .
#
#usage for one file, write results to a report file:
#docker run -v /samples:/samples cincan/pdfxray_lite -f /samples/input/sample.pdf -r /samples/output/report
#
#analyze all files in a directory:
#docker run -v /samples:/samples cincan/pdfxray_lite -d /samples/input/ -r /samples/output/report

FROM alpine:latest

RUN apk update && apk add \
	git \
	python \
	py-simplejson

RUN git clone https://github.com/9b/pdfxray_lite.git
ENTRYPOINT ["/usr/bin/python","pdfxray_lite/pdfxray_lite.py"]

