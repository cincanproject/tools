ARG tool_version=jd-cli-1.2.0

FROM alpine:3.11 as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV SHA256=ae589be342b8ea2ccfa48f9da09c78e1c54f263d6695c7a4385a9f748c22bb25

RUN apk add --no-cache wget unzip && \
    wget -q -O "jd-cli.zip" "https://github.com/kwart/jd-cli/releases/download/$TOOL_VERSION/$TOOL_VERSION-dist.zip" && \
    echo "$SHA256  jd-cli.zip" | sha256sum -c && \
    unzip -q "jd-cli.zip" -d .

FROM openjdk:8-jre-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /jd-cli.jar /usr/local/bin/

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser/
USER appuser

# Should be final modification for layers to be usable! Keep as final
COPY meta.json /opt/

ENTRYPOINT ["java", "-jar", "/usr/local/bin/jd-cli.jar"]
CMD ["--help"]
