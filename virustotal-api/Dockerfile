FROM alpine:3.9

LABEL MAINTAINER=cincan.io

RUN apk update && apk add --no-cache \
    git \
    python3 \
    py-requests \
    && git clone https://github.com/Rloota/virustotal-api-v2

WORKDIR /virustotal-api-v2
ENTRYPOINT ["/usr/bin/python3","/virustotal-api-v2/vt.py"]

CMD ["-h"]