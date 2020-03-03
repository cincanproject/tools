FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ENV VERSION=0.5.1-13

RUN apt update && apt install -y \
        steghide=$VERSION \
        && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /home/appuser

ENTRYPOINT ["steghide"]
CMD ["--help"]
