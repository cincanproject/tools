#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Example command to use apktool
#docker run --rm -v `pwd`:/appA 

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io
#LABEL io.cincan.input= "application/apk, application/jar"
#LABEL io.cincan.output=""
#COPY cincan /cincan

#Define apktool version
ENV JD_CMD_VERSION=1.0.0.Final
RUN apk add --no-cache wget unzip

#Change workdir
WORKDIR /usr/local/bin
RUN mkdir /tools

# Download and Install jd-cmd
RUN wget -q -O "jd-cmd.zip" "https://github.com/kwart/jd-cmd/releases/download/jd-cmd-$JD_CMD_VERSION/jd-cli-$JD_CMD_VERSION-dist.zip"
RUN mkdir /tools/jd-cmd
RUN unzip -q "jd-cmd.zip" -d .
RUN chmod +x "jd-cli"


VOLUME ["/appA"]

WORKDIR /appA

ENTRYPOINT ["/usr/local/bin/jd-cli"]
CMD ["--help"]
