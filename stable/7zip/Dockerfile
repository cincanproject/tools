ARG tool_version=16.02+dfsg-6

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    p7zip-full && \
    rm -rf /var/lib/apt/lists/*

USER appuser

RUN mkdir /home/appuser/tool

WORKDIR /home/appuser/tool

ENTRYPOINT ["7z"]
CMD ["-h"]
