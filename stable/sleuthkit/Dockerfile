### Usage: docker run -it -v `pwd`/samples:/samples cincan/sleuthkit [tool from sleuthkit]
### or cincan run cincan/sleuthkit [tool from sleuthkit]

ARG tool_version=4.11.0
FROM debian:10-slim AS build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

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

RUN wget -qq https://github.com/sleuthkit/sleuthkit/archive/sleuthkit-$TOOL_VERSION.tar.gz \
    && tar xvf sleuthkit-$TOOL_VERSION.tar.gz \
    && cd sleuthkit-sleuthkit-$TOOL_VERSION \
    && ls -la \
    && ./bootstrap \
    && ./configure \
    && make \
    && make install 

FROM debian:10-slim as runtime

COPY --from=build /usr/local/bin /usr/local/bin

ARG tool_version
ENV TOOL_VERSION=$tool_version

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

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["/entrypoint.sh"]
CMD ["help"]
