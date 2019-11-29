#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io

#Define apktool version
ENV VERSION=2.4.0

RUN apk add --no-cache curl bash


# Add an user
RUN mkdir -p /home/appuser \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

#change user and workdir
USER appuser

RUN mkdir -p ~/.local/share/apktool/framework

WORKDIR /home/appuser

#Download Linux wrapper script and give it right permissions
RUN curl -sLO https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool && chmod +x apktool
#Download apktool and give it right permissions
RUN curl -sL -o apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_$VERSION.jar && chmod +x apktool.jar

ENTRYPOINT ["/home/appuser/apktool"]
