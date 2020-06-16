# Testcomment

FROM alpine:3.8

ENV SURICATA_VER="4.1.0"

RUN apk update && apk add pcre pcre-tools pcre-dev \
    build-base python python-dev py-pip autoconf automake libtool libpcap-dev libnet-dev \
    yaml yaml-dev zlib zlib-dev libcap-ng-dev libcap-ng libnetfilter_queue-dev lz4-dev \
    make libmagic file-dev jansson-dev jansson pkgconf wget rust cargo lua-dev geoip geoip-dev \
    nss nss-dev nspr nspr-dev \
    && pip install --upgrade pip pyyaml && pip install --upgrade suricata-update \
    && cd /tmp \
    && wget "http://www.openinfosecfoundation.org/download/suricata-$SURICATA_VER.tar.gz" \
    && tar -xvzf "suricata-$SURICATA_VER.tar.gz" \
    && cd suricata-$SURICATA_VER \
    && ./configure --enable-nfqueue --enable-lua --disable-gccmarch-native --enable-geopip --prefix=/usr --sysconfdir=/etc --localstatedir=/var && make\
    && make install-full \
    && make clean \
    && rm -rf /tmp/suricata-$SURICATA_VER \
    && rm "/tmp/suricata-$SURICATA_VER.tar.gz"

COPY suricata.yaml /etc/suricata/suricata.yaml

USER root

RUN suricata-update update-sources \
    && suricata-update enable-source et/open \
    && suricata-update enable-source oisf/trafficid \
    && suricata-update enable-source ptresearch/attackdetection \
    && suricata-update enable-source sslbl/ssl-fp-blacklist \
    && suricata-update enable-source etnetera/aggressive \
    && suricata-update

ENTRYPOINT ["suricata"]
