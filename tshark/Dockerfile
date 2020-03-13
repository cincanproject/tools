FROM alpine:latest

LABEL MAINTAINER=cincan.io
ENV VERSION=3.0.9-r0

RUN apk update && apk add --no-cache tshark=${VERSION}

# Add an user
RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser && \
    addgroup tshark && \
    addgroup appuser tshark  && \
    chgrp tshark /usr/bin/dumpcap && \
    chmod o-rx /usr/bin/dumpcap && \
    setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap && \
    getcap /usr/bin/dumpcap

USER appuser
WORKDIR /home/appuser

ENTRYPOINT ["tshark"]
CMD ["--help"]
