#Dex files to jar

#Example command to use dex2jar
#docker run --rm -v `pwd`:/appB dex-tools 

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io
#LABEL io.cincan.input= "application/apk, application/jar"
#LABEL io.cincan.output=""
#COPY cincan /cincan

#Define apktool version
ENV DEX2JAR_VERSION=2.1
RUN apk add --no-cache wget unzip

#Change workdir
WORKDIR /usr/local/bin
#RUN mkdir /tools

#Download dex2jar tool  and give it right permissions
RUN wget -q -O "dex-tools.zip" "https://github.com/pxb1988/dex2jar/files/1867564/dex-tools-2.1-SNAPSHOT.zip"
RUN unzip -q "dex-tools.zip" -d .
#RUN mv "/tools/dex-tools-$DEX2JAR_VERSION-SNAPSHOT/" "/usr/local/bin/tools"
#RUN find "." -type f -name \*.sh -print -exec chmod +x {} \;
RUN chmod +x ./dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh

VOLUME ["/appB"]

WORKDIR /appB

ENTRYPOINT ["/usr/local/bin/dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh"]
