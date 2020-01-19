#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Example command to use jd-cmd tool
#docker run --rm -v `pwd`:/data jdcli

#Java 1.8 is needed
FROM openjdk:8-jre-alpine

LABEL MAINTAINER=cincan.io

#Define jd-cmd version
ENV VERSION=1.0.0.Final
RUN apk add --no-cache wget unzip

#Change workdir
WORKDIR /usr/local/bin

# Download,  unzip and give permissions to jd-cmd
RUN wget -q -O "jd-cmd.zip" "https://github.com/kwart/jd-cmd/releases/download/jd-cmd-$VERSION/jd-cli-$VERSION-dist.zip"
RUN unzip -q "jd-cmd.zip" -d .
RUN chmod +x "jd-cli"


VOLUME ["/data"]

WORKDIR /data

ENTRYPOINT ["/usr/local/bin/jd-cli"]
CMD ["--help"]
