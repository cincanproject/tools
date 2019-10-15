FROM alpine:3.9
LABEL maintainer "https://gitlab.com/CinCan"

ENV VOL_VERSION 2.6.1 
ENV YARA_VERSION 3.10.0
ENV YARA_PY_VERSION 3.10.0

RUN apk --update --no-cache add git \
    bison \
    ca-certificates \
    file \
    jansson \
    openssl \
    py-crypto \
    py-lxml \
    py-pillow \
    py-setuptools \
    python \
    su-exec \
    tini \
    unzip \
    zlib \
    && rm -rf /var/lib/apt/lists/*

RUN apk add --no-cache -t .build-deps \
    py-setuptools \
    openssl-dev \
    jansson-dev \
    python-dev \
    build-base \
    zlib-dev \
    libc-dev \
    file-dev \
    jpeg-dev \
    automake \
    autoconf \
    libtool \
    flex \
    py-pip \
    && export PIP_NO_CACHE_DIR=off \
    && export PIP_DISABLE_PIP_VERSION_CHECK=on \
    && pip install --upgrade pip==18.1 wheel \
    && pip install simplejson \
    construct \
    openpyxl \
    haystack \
    distorm3 \
    colorama \
    ipython \
    pycoin \
    pytz \
    && set -x \
    && cd /tmp \
    && echo "===> Installing Yara from source..." \
    && git clone --recursive --branch v$YARA_VERSION https://github.com/VirusTotal/yara.git \
    && cd /tmp/yara \
    && ./bootstrap.sh \
    && sync \
    && ./configure --with-crypto \
    --enable-magic \
    --enable-cuckoo \
    --enable-dotnet \
    && make \
    && make install \
    && echo "===> Installing yara-python from source..." \
    && cd /tmp/ \
    && git clone --recursive --branch v$YARA_PY_VERSION https://github.com/VirusTotal/yara-python \
    && cd yara-python \
    && python setup.py build --dynamic-linking \
    && python setup.py install \
    && echo "===> Installing Volatility from source..." \
    && cd /tmp/ \
    && git clone --recursive --branch $VOL_VERSION https://github.com/volatilityfoundation/volatility.git \
    && cd volatility \
    && python setup.py build install \
    && rm -rf /tmp/* \
    && apk del --purge .build-deps

VOLUME ["/samples"]
VOLUME ["/plugins"]
WORKDIR /volatility
ENTRYPOINT ["vol.py"]
CMD ["--help"]