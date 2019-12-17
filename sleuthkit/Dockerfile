### Usage: docker run -it -v `pwd`/samples:/samples cincan/sleuthkit [tool from sleuthkit]
### or cincan run cincan/sleuthkit [tool from sleuthkit]

FROM debian:10-slim AS build

ENV VERSION=4.7.0

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    autotools-dev \
    autoconf \
    automake \
    libtool \
    zlib1g-dev \
    libewf-dev \
    libvhdi-dev \
    libvmdk-dev \
    ca-certificates \
    wget

RUN wget -qq https://github.com/sleuthkit/sleuthkit/archive/sleuthkit-$VERSION.tar.gz \
    && tar xvf sleuthkit-$VERSION.tar.gz \
    && cd sleuthkit-sleuthkit-$VERSION \
    && ls -la \
    && ./bootstrap \
    && ./configure \
    && make \
    && make install 

FROM debian:10-slim as runtime

COPY --from=build /usr/local/bin /usr/local/bin

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    zlib1g \
    libewf2 \
    libvhdi1 \
    libvmdk1 \
    file \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh && \
    groupadd -g 1000 app && \
    useradd -u 1000 -s /sbin/nologin appuser

USER appuser
WORKDIR "/home/appuser/"

ENTRYPOINT ["/entrypoint.sh"]
CMD ["help"]
