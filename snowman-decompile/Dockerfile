# Snowman decompiler, https://derevenets.com/
# docker run -v /samples:/samples cincan/snowman-decompile /samples/executable

FROM debian:9-slim

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install --no-install-recommends -y \
    unzip=6.0-21+deb9u1 \
    wget=1.18-5+deb9u3 \
    ca-certificates=20161130+nmu1+deb9u1 \
    build-essential=12.3 \
    cmake=3.7.2-1 \
    libboost-dev=1.62.0.1 \
    qt5-default=5.7.1+dfsg-3+deb9u1 \
    ninja-build=1.7.2-1 \
    && wget -q https://github.com/yegord/snowman/archive/master.zip \
    && unzip master.zip \
    && rm master.zip \
    && make -C /snowman-master \
    && apt-get clean \
    && apt-get --purge remove -y unzip wget ca-certificates build-essential cmake ninja-build \
    && apt-get --purge -y autoremove \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown -R appuser /tmp/snowman.ed3979dabdbc311f6c973f6a61c8c6b220b0e41b

USER appuser

ENTRYPOINT ["/snowman-master/build/nocode/nocode"]
CMD ["--help"]
