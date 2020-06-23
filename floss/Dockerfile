ARG tool_version=1.5.0

FROM debian:buster-slim as builder
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV DOWNLOAD_URL=https://github.com/fireeye/flare-floss/releases/download/v$TOOL_VERSION/floss-${TOOL_VERSION}-GNU.Linux.zip

RUN apt-get update && apt-get -y install \
    unzip \
    wget

RUN mkdir /floss \
    && cd /floss \
    && wget ${DOWNLOAD_URL} \
    && unzip floss-${TOOL_VERSION}-GNU.Linux.zip \
    && chmod +x floss

FROM debian:buster-slim as runtime

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=builder /floss/floss /floss

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && chown appuser /floss

WORKDIR /home/appuser/
USER appuser

ENTRYPOINT ["/floss"]
CMD ["--help"]
