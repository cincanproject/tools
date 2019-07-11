# John the Ripper for extracting hash from PDF files.
#
# build:
# docker build -t cincan/pdf2john .
#
# usage:
# docker run -v /samples:/samples cincan/pdf2john /samples/encrypted.pdf


FROM alpine:3.10

RUN apk update && apk add --no-cache \
    git \
    perl \
    exiftool \
    && git clone https://github.com/magnumripper/JohnTheRipper.git

ENTRYPOINT ["/usr/bin/perl","/JohnTheRipper/run/pdf2john.pl"]
