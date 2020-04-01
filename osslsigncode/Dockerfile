ARG tool_version=2.0-1

FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt update && apt install -y \
        osslsigncode=$TOOL_VERSION \
        && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["osslsigncode"]
CMD ["-h"]
