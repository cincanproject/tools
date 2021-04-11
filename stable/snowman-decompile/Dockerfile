# Snowman decompiler, https://derevenets.com/
# docker run -v /samples:/samples cincan/snowman-decompile /samples/executable

ARG tool_version=0.1.3

FROM debian:10-slim

LABEL MAINTAINER=cincan.io


ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV SNOWMAN_SHA256 6baf2e2dc2e66e43f708b5ee7490b08676e0756a04f059b3b6be5fe3ec385cd5


RUN apt-get update && apt-get install --no-install-recommends -y \
    unzip \
    wget \
    ca-certificates \
    build-essential \
    cmake \
    libboost-dev \
    qt5-default \
    ninja-build \
    && wget -q "https://github.com/yegord/snowman/archive/v${TOOL_VERSION}.zip" \
    && echo "${SNOWMAN_SHA256}  v${TOOL_VERSION}.zip" | sha256sum -c - \
    && unzip "v${TOOL_VERSION}.zip" \
    && rm "v${TOOL_VERSION}.zip" \
    && mv "snowman-${TOOL_VERSION}" "snowman-master" \
    && make -C /snowman-master \
    && apt-get clean \
    && apt-get --purge remove -y unzip wget ca-certificates build-essential cmake ninja-build \
    && apt-get --purge -y autoremove \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown -R appuser /tmp/snowman.ed3979dabdbc311f6c973f6a61c8c6b220b0e41b

USER appuser
WORKDIR /home/appuser
# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["/snowman-master/build/nocode/nocode"]
CMD ["--help"]
