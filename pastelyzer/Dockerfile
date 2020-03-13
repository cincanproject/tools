FROM debian:10-slim as build

LABEL MAINTAINER=cincan.io

ENV DEBIAN_FRONTEND=noninteractive
ENV VERSION 0.8.1-beta
ENV PASTELYZER_SHA256 05d259b9dbdbfdbc8366a62be8bdaa840cd641a0b2e0cc4544db73eee2ce5737

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates \
    curl sbcl

RUN curl -LO https://github.com/cert-lv/pastelyzer/releases/download/rel-0.8.1-beta/pastelyzer-"${VERSION}".tgz && \
    echo "$PASTELYZER_SHA256 pastelyzer-${VERSION}.tgz" | sha256sum -c -  && \
    tar -xvzf pastelyzer-${VERSION}.tgz 

FROM debian:10-slim as env

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY --from=build /pastelyzer/bin/pastelyzer /usr/bin
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libssl1.1 libzmq5-dev && \
    rm -rf /var/lib/apt/lists/*

USER appuser

ENTRYPOINT ["pastelyzer"]
CMD ["-h"]
