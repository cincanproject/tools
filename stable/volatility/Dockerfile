ARG COMMIT="5f685e5"
ARG tool_version="2.6.1"
# py-crypto decprecated in 3.12
FROM alpine:3.11
LABEL maintainer=cincan.io

ARG tool_version
ARG COMMIT
ENV TOOL_VERSION="$tool_version - $COMMIT"
ENV YARA_VERSION 3.11.0
ENV YARA_PY_VERSION 3.11.0

RUN echo "$TOOL_VERSION"

RUN apk --update --no-cache add \
    bison \
    ca-certificates \
    file \
    git \
    jansson \
    openssl \
    py-crypto \
    py-lxml \
    py-pillow \
    python \
    su-exec \
    tini \
    unzip \
    zlib \
    py-setuptools \
    && rm -rf /var/lib/apt/lists/*

RUN apk add --no-cache -t build-dependencies \
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
    && pip install \
    colorama \
    construct \
    # distorm 3.5.0 breaks volatility
    distorm3==3.4.4 \
    haystack \
    ipython \
    openpyxl \
    pycoin \
    pytz \
    simplejson \
    pycrypto \
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
    && git clone --recursive https://github.com/volatilityfoundation/volatility.git \
    && cd volatility \
    && git checkout $COMMIT \
    && python setup.py build install \
    && rm -rf /tmp/* \
    && apk del --purge build-dependencies

RUN adduser -s /sbin/login -D appuser
USER appuser

WORKDIR /home/appuser/

ENTRYPOINT ["vol.py"]
CMD ["--help"]
