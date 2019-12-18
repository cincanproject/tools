FROM ubuntu:latest
LABEL maintainer=cinca.io

ENV VERSION=1.5.0
ENV DOWNLOAD_URL=https://github.com/fireeye/flare-floss/releases/download/v$VERSION/floss-${VERSION}-GNU.Linux.zip

RUN apt update && apt -y install \
    unzip \
    wget \
    && apt autoclean

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

WORKDIR /home/appuser/
RUN wget $DOWNLOAD_URL \
    && unzip floss-${VERSION}-GNU.Linux.zip \
    && chmod +x  floss \
    && chown appuser floss \
    && rm floss-${VERSION}-GNU.Linux.zip

USER appuser

ENTRYPOINT ["./floss"]
CMD ["--help"]
