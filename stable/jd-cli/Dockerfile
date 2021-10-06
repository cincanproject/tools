ARG tool_version=jd-cli-1.2.1

FROM alpine:3.11 as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV SHA256=db7f28fa5dde50211f967d08f00ef85a41d46178a035ab805f114dca0a16d3c7

RUN apk add --no-cache wget unzip maven openjdk11 && \
    wget -q -O "jd-cli.zip" "https://github.com/intoolswetrust/jd-cli/archive/refs/tags/${TOOL_VERSION}.zip" && \
    echo "$SHA256  jd-cli.zip" | sha256sum -c && \
    unzip -q "jd-cli.zip" -d . && \
    mv "jd-cli-$TOOL_VERSION" jd-cli && \
    cd jd-cli && \
    mvn package 

FROM openjdk:8-jre-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /jd-cli/jd-cli/target/jd-cli.jar /usr/local/bin/

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser/
USER appuser

# Should be final modification for layers to be usable! Keep as final
COPY meta.json /opt/

ENTRYPOINT ["java", "-jar", "/usr/local/bin/jd-cli.jar"]
CMD ["--help"]
