ARG tool_version=0.6
ARG radamsa_sha256=7bf34aad41e3045cbf314d3a7077554642bd0635e629d69e254712a117952d50

FROM debian:10-slim AS builder

ARG tool_version
ARG radamsa_sha256
ENV TOOL_VERSION=$tool_version
ENV RADAMSA_SHA256=$radamsa_sha256

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    git \
    ca-certificates \
    pkg-config \
    libboost-dev \
    wget \ 
    unzip

RUN wget -O /tmp/radamsa.zip https://gitlab.com/akihe/radamsa/-/archive/v$TOOL_VERSION/radamsa-v$TOOL_VERSION.zip &&\
    echo "$RADAMSA_SHA256 /tmp/radamsa.zip" | sha256sum -c - &&\
    unzip /tmp/radamsa.zip &&\
    cd "radamsa-v$TOOL_VERSION" &&\
    make && make install 

FROM gcr.io/distroless/base-debian10 AS production

ARG tool_version
ENV TOOL_VERSION=$tool_version

USER nonroot
WORKDIR /home/nonroot/tool
COPY --from=builder /radamsa-v$TOOL_VERSION/bin/radamsa /home/nonroot/

# Should be kept as final modification for layers - fetched separately
COPY meta.json /opt/

ENTRYPOINT ["/home/nonroot/radamsa"]
CMD ["--help"]
