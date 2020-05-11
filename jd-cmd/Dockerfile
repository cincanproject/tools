ARG tool_version=1.0.1.Final

FROM alpine:3.11 as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV SHA256=767013796e7696854ff8b1ed0a9d4c12e4bed941be0c23537c7a2cadc5022340

RUN apk add --no-cache wget unzip && \
    wget -q -O "jd-cmd.zip" "https://github.com/kwart/jd-cmd/releases/download/jd-cmd-$TOOL_VERSION/jd-cli-$TOOL_VERSION-dist.zip" && \
    echo "$SHA256  jd-cmd.zip" | sha256sum -c && \
    unzip -q "jd-cmd.zip" -d .

FROM openjdk:8-jre-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /jd-cli.jar /usr/local/bin/

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser/
USER appuser

ENTRYPOINT ["java", "-jar", "/usr/local/bin/jd-cli.jar"]
CMD ["--help"]
