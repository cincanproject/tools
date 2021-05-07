ARG tool_version=3.4.5-r0

FROM alpine:latest

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk update && apk add --no-cache tshark=${TOOL_VERSION}

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
# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["tshark"]
CMD ["--help"]
