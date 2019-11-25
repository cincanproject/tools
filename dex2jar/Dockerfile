#Dex files to jar

#Example command to use dex2jar tool with docker
#docker run --rm -v `pwd`:/samples dex2jar path/to/your/.apk

#Base image
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io

#Define apktool version
ENV VERSION=2.1
RUN apk add --no-cache wget unzip

#Change workdir
WORKDIR /usr/local/bin

#Download dex2jar tool, unzip it and give it right permissions
RUN wget -q -O "dex-tools.zip" "https://github.com/pxb1988/dex2jar/files/1867564/dex-tools-$VERSION-SNAPSHOT.zip"
RUN unzip -q "dex-tools.zip" -d .
RUN chmod +x ./dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh

VOLUME ["/samples"]

WORKDIR /samples

ENTRYPOINT ["/usr/local/bin/dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh"]
