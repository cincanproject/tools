FROM debian:9-slim

LABEL MAINTAINER=cincan.io

RUN apt-get update && apt-get install -y \
        ca-certificates \
        git \
        python3-dev \
        python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/CERTCC/keyfinder.git \
    && pip3 install androguard==3.3.5 \
         python-magic==0.4.15 \
         PyOpenSSL==19.00 \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

ENTRYPOINT ["/usr/bin/python3", "keyfinder/keyfinder.py"]


