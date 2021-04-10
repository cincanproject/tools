ARG tool_version=2.0-1

FROM debian:10-slim
# TODO update into bullseye when released

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y \
        osslsigncode=$TOOL_VERSION \
        && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /home/appuser

COPY meta.json /opt/

ENTRYPOINT ["osslsigncode"]
CMD ["-h"]
