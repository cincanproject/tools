FROM debian:9-slim
USER root
#RUN apk update && apk add --no-cache git gcc g++ \
RUN apt-get update && apt-get install -y \
    ca-certificates git python3-dev python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/CERTCC/keyfinder.git \
    && pip3 install androguard python-magic PyOpenSSL

ENTRYPOINT ["/usr/bin/python3", "keyfinder/keyfinder.py"]


