ARG tool_version=1.5.0

FROM debian:buster-slim
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DOWNLOAD_URL=https://github.com/fireeye/flare-floss/releases/download/v$TOOL_VERSION/floss-${TOOL_VERSION}-GNU.Linux.zip

RUN apt-get update && apt-get -y install \
    unzip \
    wget

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

RUN mkdir /floss \
    && cd /floss \
    && wget ${DOWNLOAD_URL} \
    && unzip floss-${TOOL_VERSION}-GNU.Linux.zip \
    && chmod +x floss \
    && chown appuser floss \
    && rm floss-${TOOL_VERSION}-GNU.Linux.zip \
    && apt -y remove unzip wget

WORKDIR /home/appuser/
USER appuser

ENTRYPOINT ["/floss/floss"]
CMD ["--help"]
