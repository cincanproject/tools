# Dockerfile for Concourse worker

FROM ubuntu:18.04

RUN sed -i 's/# deb/deb/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
        wget \
        iproute2 \
        ca-certificates \
        iputils-ping &&\
        apt-get clean &&\
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget --progress=dot:giga -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN wget --progress=dot:giga -O /usr/local/bin/concourse https://github.com/concourse/concourse/releases/download/v4.2.2/concourse_linux_amd64
RUN chmod +x /usr/local/bin/concourse

RUN mkdir /etc/concourse
RUN mkdir -p /opt/concourse/worker

VOLUME /etc/concourse

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/local/bin/concourse"]
