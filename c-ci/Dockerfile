# Dockerfile for Concourse CI

FROM ubuntu:18.04

RUN sed -i 's/# deb/deb/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
        wget \
        iproute2 \
        ca-certificates \
        iputils-ping \
        git \
        ssh &&\
        apt-get clean &&\
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN wget -O /usr/local/bin/concourse https://github.com/concourse/concourse/releases/download/v4.1.0/concourse_linux_amd64
RUN chmod +x /usr/local/bin/concourse

RUN wget -O /usr/local/bin/fly https://github.com/concourse/concourse/releases/download/v4.1.0/fly_linux_amd64
RUN chmod +x /usr/local/bin/fly

RUN mkdir /etc/concourse
VOLUME /etc/concourse

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/local/bin/concourse"]