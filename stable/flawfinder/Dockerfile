ARG tool_version=2.0.17
ARG SHA256=eb00fb26e6ff19d9b953101217ebd0c00c35dbf58553cc7ebf9b14ced958cb93
FROM alpine:3.15

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

COPY meta.json /opt/

ENTRYPOINT ["flawfinder"]
CMD ["--help"]
