# Java Decompiler

FROM openjdk:8-alpine as build

LABEL MAINTAINER=cincan.io

ENV FERNFLOWER_VERSION=8b1358fa509b209b72f8e8ac832fa5043b56bf57
ENV FERNFLOWER_SHA256 49d788b4eee6e27d2c394564719b1f9c97b7269240a27a4446a866e4ab319fc4
ENV FERNFLOWER_LOC=intellij-community-$FERNFLOWER_VERSION/plugins/java-decompiler/engine
ENV DEBIAN_FRONTEND=noninteractive

RUN apk add --no-cache wget unzip && \
    wget -q -O archive.zip https://github.com/JetBrains/intellij-community/archive/$FERNFLOWER_VERSION.zip

RUN echo "$FERNFLOWER_SHA256  archive.zip" | sha256sum -c - \
	&& unzip archive.zip $FERNFLOWER_LOC/*

RUN ls -la $FERNFLOWER_LOC
RUN cd $FERNFLOWER_LOC && \
    chmod +x gradlew && \
    ./gradlew jar --no-daemon && \
    mv build/libs/fernflower.jar /

FROM openjdk:8-jre-alpine as env

COPY --from=build /fernflower.jar /app/fernflower.jar

RUN mkdir -p /home/appuser/tool \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

USER appuser
WORKDIR /home/appuser/tool

ENTRYPOINT ["java", "-jar", "/app/fernflower.jar"]
