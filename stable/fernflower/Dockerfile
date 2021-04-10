# Java Decompiler
ARG tool_version=idea/211.6693.111 

# FROM openjdk:11-alpine as build
FROM adoptopenjdk/openjdk11:alpine as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=${tool_version}
ENV TOOL_SHA256 9f9ca666985c9b55eb9ab0e3418cf4ea9266bf35f35caf9e915596df74eacada
ENV DEBIAN_FRONTEND=noninteractive

RUN apk add --no-cache wget unzip && \
    wget -q -O archive.zip https://github.com/JetBrains/intellij-community/archive/$TOOL_VERSION.zip

RUN FERNFLOWER_LOC=intellij-community-$(echo $TOOL_VERSION | tr / -)/plugins/java-decompiler/engine && \
    echo "$TOOL_SHA256  archive.zip" | sha256sum -c - \
    && unzip archive.zip $FERNFLOWER_LOC/* && \
    cd $FERNFLOWER_LOC && \
    chmod +x gradlew && \
    ./gradlew jar --no-daemon && \
    mv build/libs/fernflower.jar /

# FROM openjdk:8-jre-alpine as env
FROM adoptopenjdk/openjdk11:alpine-jre as env
ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /fernflower.jar /app/fernflower.jar

RUN mkdir -p /home/appuser/tool \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

USER appuser
WORKDIR /home/appuser/tool

COPY meta.json /opt/

ENTRYPOINT ["java", "-jar", "/app/fernflower.jar"]
