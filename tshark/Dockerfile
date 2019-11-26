FROM alpine:3.10

LABEL MAINTAINER=cincan.io
ENV VERSION=3.0.4-r0

RUN apk update && apk add --no-cache tshark=${VERSION}

ENTRYPOINT ["tshark"]
CMD ["--help"]

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
