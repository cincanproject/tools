ARG tool_version=0.149
ARG dist_sha256=db683b5b3bc2c20fd2fabcc9d749d5b8bcbba736f334e5ac2092173242967aca

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

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser/
USER appuser

ENTRYPOINT ["java", "-jar", "/usr/bin/cfr.jar"]
CMD ["--help"]
