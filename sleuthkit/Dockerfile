### Usage: docker run -it -v `pwd`/samples:/samples cincan/sleuthkit [tool from sleuthkit]

FROM debian:9-slim

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
    && git clone --depth 1 https://github.com/sleuthkit/sleuthkit.git

WORKDIR sleuthkit
RUN ./bootstrap \
    && ./configure \
    && make \
    && make install 

WORKDIR /
RUN rm -r sleuthkit

CMD fls
