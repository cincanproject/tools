#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Example command to use apktool
#docker run --rm -v `pwd`:/app apktool d apk_file.apk

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io
#LABEL io.cincan.input= "application/apk, application/jar"
#LABEL io.cincan.output=""
#COPY cincan /cincan

#Define apktool version
ENV APKTOOL_VERSION=2.4.0
RUN apk add --no-cache curl bash

#Change workdir
WORKDIR /usr/local/bin

#Download Linux wrapper script and give it right permissions
RUN curl -sLO https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool && chmod +x apktool
#Download apktool and give it right permissions
RUN curl -sL -o apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_${APKTOOL_VERSION}.jar && chmod +x apktool.jar

# Create alias command
#RUN echo 'alias apktool="docker run --rm -v `pwd`:/app apktool"' >> ~/.bashrc

VOLUME ["/app"]

WORKDIR /app 

ENTRYPOINT ["apktool"]
CMD ["--help"]
