# Dockerfile for Concourse CI
FROM debian:8.11-slim

LABEL MAINTAINER=cincan.io

RUN sed -i 's/# deb/deb/g' /etc/apt/sources.list \
    && apt-get update && apt-get install -y \
        wget \
        iproute2 \
        ca-certificates \
        iputils-ping \
        git \
        ssh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
    && chmod +x /usr/local/bin/dumb-init \
    && wget --progress=dot:giga -O /usr/local/bin/concourse https://github.com/concourse/concourse/releases/download/v4.2.2/concourse_linux_amd64 \
    && chmod +x /usr/local/bin/concourse \
    && wget --progress=dot:giga -O /usr/local/bin/fly https://github.com/concourse/concourse/releases/download/v4.2.2/fly_linux_amd64 \
    && chmod +x /usr/local/bin/fly \
    && mkdir /etc/concourse \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

VOLUME /etc/concourse

EXPOSE 8080

USER appuser

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/local/bin/concourse"]
