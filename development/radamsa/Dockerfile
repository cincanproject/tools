ARG tool_version=0.6

FROM debian:10-slim AS builder

ARG tool_version
ENV TOOL_VERSION=$tool_version

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    git \
    ca-certificates \
    pkg-config \
    libboost-dev \
    wget

RUN git clone --branch=v$TOOL_VERSION https://gitlab.com/akihe/radamsa.git &&\
    cd radamsa &&\
    make && make install

FROM gcr.io/distroless/base-debian10 AS production

ARG tool_version
ENV TOOL_VERSION=$tool_version

WORKDIR /home/appuser
COPY --from=builder /radamsa/bin/radamsa /home/appuser/

ENTRYPOINT ["/home/appuser/radamsa"]
CMD ["--help"]
