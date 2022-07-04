ARG tool_version=rel-0.11.1-beta

FROM debian:10-slim as build
LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates \
    curl sbcl

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates build-essential curl git libssl-dev libzmq5-dev sbcl

RUN curl -O https://beta.quicklisp.org/quicklisp.lisp && \
    sbcl --load quicklisp.lisp \
       --eval '(quicklisp-quickstart:install)' \
       --quit

RUN git clone --recurse-submodules --depth=1 --branch=$TOOL_VERSION https://github.com/cert-lv/pastelyzer.git && \
    cd pastelyzer && \
    bin/build.sh load-deps && \
    bin/build.sh

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

COPY --from=build /pastelyzer/bin/pastelyzer /usr/bin
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libssl1.1 libzmq5-dev && \
    rm -rf /var/lib/apt/lists/*

USER appuser
COPY meta.json /opt/
ENTRYPOINT ["pastelyzer"]
CMD ["-h"]
