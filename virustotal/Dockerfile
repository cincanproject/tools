# Retrieves file or url results from VirusTotal
# By default only sends hash of a file to check if the file has already been analyzed
# It's possible to send the whole file if report doesn't exist with --send argument
#
# build:
# docker build -t cincan/virustotal .
#
# usage (urls, scans all urls in the newline delimited file):
# docker run -v /files:/files cincan/virustotal --output /files/ --url_file /files/url_file [options]
# usage (files, scans all files in the folder):
# docker run -v /files:/files cincan/virustotal --output /files/ --files /files/ [options]
#
# [options]
# [--send, -s] Sends file or url to be analyzed if existing report doesn't exist
# [--verbose, -v] Sets verbosity to high

FROM python:3.6-alpine

LABEL MAINTAINER=cincan.io

COPY /virustotal .

RUN pip3 install -r requirements.txt \
    && adduser -s /sbin/login -D appuser

USER appuser

ENTRYPOINT ["python3", "virustotal.py"]
