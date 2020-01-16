FROM debian:10-slim as build

LABEL MAINTAINER=cincan.io

ENV DEBIAN_FRONTEND=noninteractive
env VERSION=002a853a0fdd79a15c05eb8d31d73dd5ff12f67d

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates build-essential curl git libssl-dev libzmq5-dev sbcl

RUN curl -O https://beta.quicklisp.org/quicklisp.lisp && \
    sbcl --load quicklisp.lisp \
       --eval '(quicklisp-quickstart:install)' \
       --quit

RUN git clone --recurse-submodules --depth=1 https://github.com/cert-lv/pastelyzer.git && \
    cd pastelyzer && \
    git checkout $VERSION && \
    bin/build.sh load-deps && \
    bin/build.sh

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
