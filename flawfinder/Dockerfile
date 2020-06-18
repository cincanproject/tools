ARG tool_version=2.0.11
FROM alpine:latest
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV FLAWFINDER_SHA256 f67ed6af5fd9e15737908233f9c4563fb5c5702d3a023b30d3c03d21c7bcd744

RUN apk update && apk add --no-cache \
    make \
    python2

RUN wget -q -O "flawfinder-${TOOL_VERSION}.zip" "https://github.com/david-a-wheeler/flawfinder/archive/$TOOL_VERSION.zip" \
    && echo "$FLAWFINDER_SHA256  flawfinder-${TOOL_VERSION}.zip" | sha256sum -c - \
    && unzip -q "flawfinder-${TOOL_VERSION}.zip" \
    && cd flawfinder-${TOOL_VERSION} \
    && make install \
    && adduser -s /sbin/nologin -D appuser

WORKDIR /home/appuser/
USER appuser
ENTRYPOINT ["flawfinder"]
