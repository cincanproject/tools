FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ENV VERSION=2.0-1

RUN apt update && apt install -y \
        osslsigncode=$VERSION \
        && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["osslsigncode"]
CMD ["-h"]
