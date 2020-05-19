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

FROM debian:10-slim AS production

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /radamsa/bin/radamsa /usr/local/bin

RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /sbin/nologin appuser

USER appuser
WORKDIR /home/appuser

ENTRYPOINT ["radamsa"]
CMD ["--help"]
