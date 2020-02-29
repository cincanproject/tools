FROM alpine:3.7 as build

LABEL MAINTAINER=cincan.io

ENV VERSION=1.0.1.Final
ENV SHA256=767013796e7696854ff8b1ed0a9d4c12e4bed941be0c23537c7a2cadc5022340

RUN apk add --no-cache wget unzip && \
    wget -q -O "jd-cmd.zip" "https://github.com/kwart/jd-cmd/releases/download/jd-cmd-$VERSION/jd-cli-$VERSION-dist.zip" && \
    echo "$SHA256  jd-cmd.zip" | sha256sum -c && \
    unzip -q "jd-cmd.zip" -d . && \
    chmod +x "jd-cli"

FROM openjdk:8-jre-slim

COPY --from=build /jd-cli.jar /usr/local/bin/

RUN adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir -p /home/appuser/tool && \
    chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser/
USER appuser

ENTRYPOINT ["java", "-jar", "/usr/local/bin/jd-cli.jar"]
CMD ["--help"]
