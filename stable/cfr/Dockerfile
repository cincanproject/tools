ARG tool_version=0.150
ARG dist_sha256=d2755995ba1f3994d71d1905544b250c49ac6529433eb4383923430b6f109826

FROM alpine:3.11 as build

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

ENTRYPOINT ["java", "-jar", "/usr/bin/cfr.jar"]
CMD ["--help"]
