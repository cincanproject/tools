# Snowman decompiler, https://derevenets.com/
# docker run -v /samples:/samples cincan/snowman-decompile /samples/executable

FROM ubuntu:18.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    unzip \
    wget \
    ca-certificates \
    build-essential \
    cmake \
    libboost-dev \
    qt5-default \
    ninja-build \
    && wget -q https://github.com/yegord/snowman/archive/master.zip \
    && unzip master.zip \
    && make -C /snowman-master \
    && apt-get clean \
    && apt-get --purge remove -y unzip wget ca-certificates build-essential cmake ninja-build \
    && apt-get --purge -y autoremove \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown -R appuser /tmp/snowman.ed3979dabdbc311f6c973f6a61c8c6b220b0e41b

USER appuser

ENTRYPOINT ["/snowman-master/build/nocode/nocode"]
CMD ["--h"]
