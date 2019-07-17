### Usage: docker run -it -v `pwd`/samples:/samples cincan/sleuthkit [tool from sleuthkit]

FROM debian:9-slim

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    autotools-dev \
    autoconf \
    automake \
    libtool \
    man \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && git clone --depth 1 https://github.com/sleuthkit/sleuthkit.git \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

WORKDIR sleuthkit
RUN ./bootstrap \
    && ./configure \
    && make \
    && make install 

WORKDIR /
RUN rm -r sleuthkit

USER appuser

CMD fls
