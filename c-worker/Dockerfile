FROM alpine:3.10

#RUN sed -i 's/# deb/deb/g' /etc/apt/sources.list

RUN apk update && apk add --no-cache \
        wget=1.20.3-r0 \
        iproute2=4.20.0-r1 \
        ca-certificates=20190108-r0 \
        iputils=20180629-r1 \
        git=2.22.0-r0

RUN wget --progress=dot:giga -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 && \
    chmod +x /usr/local/bin/dumb-init && \
    wget --progress=dot:giga -O /usr/local/bin/concourse https://github.com/concourse/concourse/releases/download/v4.2.2/concourse_linux_amd64 && \
    chmod +x /usr/local/bin/concourse && \
    mkdir /etc/concourse && \
    mkdir -p /opt/concourse/worker

VOLUME /etc/concourse

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/local/bin/concourse"]
