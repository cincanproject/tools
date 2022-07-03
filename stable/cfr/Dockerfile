ARG tool_version=0.151
ARG dist_sha256=316e9015b9af2953fcff4fe86bf3bba705f32e7cd25bd6e535c698de8a25e837

FROM alpine:latest as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ARG dist_sha256
ENV TOOL_VERSION=$tool_version
ENV SHA256=$dist_sha256

RUN apk add --no-cache wget && \
    wget -q -O "cfr.jar" "https://github.com/leibnitz27/cfr/releases/download/$TOOL_VERSION/cfr-$TOOL_VERSION.jar" && \
    echo "$SHA256  cfr.jar" | sha256sum -c

FROM openjdk:8-jre-slim

COPY --from=build /cfr.jar /usr/bin/

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser/
USER appuser
COPY meta.json /opt/

ENTRYPOINT ["java", "-jar", "/usr/bin/cfr.jar"]
CMD ["--help"]
