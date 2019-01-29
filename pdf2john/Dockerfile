# John the Ripper for extracting hash from PDF files.
#
# build:
# docker build -t cincan/pdf2john .
#
# usage:
# docker run -v /samples:/samples cincan/pdf2john /samples/encrypted.pdf


FROM alpine:latest

RUN apk update && apk add \
        git \
        perl \
        exiftool

RUN git clone https://github.com/magnumripper/JohnTheRipper.git

ENTRYPOINT ["/usr/bin/perl","/JohnTheRipper/run/pdf2john.pl"]
