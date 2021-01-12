ARG tool_version=2.0.15
ARG SHA256=a3aa71de70b2ab5433fca5a7cf597e913c05155407f4e0a1881c52ee7115f2a7
FROM alpine:latest
LABEL MAINTAINER=cincan.io

ARG tool_version
ARG SHA256
ENV TOOL_VERSION=$tool_version

ENV FLAWFINDER_SHA256=$SHA256 

RUN apk update && apk add --no-cache \
    make \
    python2

RUN wget -q -O "flawfinder-${TOOL_VERSION}.zip" "https://github.com/david-a-wheeler/flawfinder/archive/$TOOL_VERSION.zip" \
    && echo "$FLAWFINDER_SHA256  flawfinder-${TOOL_VERSION}.zip" | sha256sum -c - \
    && unzip -q "flawfinder-${TOOL_VERSION}.zip" \
    && cd flawfinder-${TOOL_VERSION} \
    && make install \
    && adduser -s /sbin/nologin -D appuser \
    && rm "../flawfinder-${TOOL_VERSION}.zip"

WORKDIR /home/appuser/
USER appuser
ENTRYPOINT ["flawfinder"]
