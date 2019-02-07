FROM alpine:3.7
LABEL maintainer "https://gitlab.com/CinCan"

ENV VOL_VERSION 2.6.1 


RUN apk --update add git openssh unzip && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

# Volatility Dependencies
RUN apk add --no-cache ca-certificates zlib py-pillow py-crypto py-lxml py-setuptools
RUN apk add --no-cache -t .build-deps \
  openssl-dev \
  python-dev \
  build-base \
  zlib-dev \
  libc-dev \
  jpeg-dev \
  automake \
  autoconf \
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
  && cd /tmp \
  && echo "===> Installing Volatility from source..." \
  && git clone --recursive --branch $VOL_VERSION https://github.com/volatilityfoundation/volatility.git \
  && cd volatility \
  && python setup.py build install \
  && rm -rf /tmp/* \
  && apk del --purge .build-deps
VOLUME ["/samples"]
VOLUME ["/plugins"]
WORKDIR /volatility
ENTRYPOINT ["vol.py"]
CMD ["-h"]