#Analyzes Android apk files using apktool 
ARG tool_version=2.4.1
#Java 1.8 is needed
FROM openjdk:8-jre-alpine

ARG tool_version
LABEL MAINTAINER=cincan.io

#Define apktool version
ENV TOOL_VERSION=${tool_version}

RUN apk add --no-cache curl bash

# Add an user
RUN mkdir -p /home/appuser/tool \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

#change user and workdir
USER appuser

RUN mkdir -p /home/appuser/.local/share/apktool/framework

WORKDIR /home/appuser/tool

#Download Linux wrapper script and give it right permissions
RUN curl -sLO https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool && chmod +x apktool
#Download apktool, make sha256 checksum and give apktool right permissions
RUN curl -sLO https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_${TOOL_VERSION}.jar  && echo "bdeb66211d1dc1c71f138003ce35f6d0cd19af6f8de7ffbdd5b118d02d825a52  apktool_${TOOL_VERSION}.jar" | sha256sum -c 
RUN mv apktool_${TOOL_VERSION}.jar apktool.jar && chmod +x apktool.jar

WORKDIR /home/appuser/

ENTRYPOINT ["/home/appuser/tool/apktool"]
