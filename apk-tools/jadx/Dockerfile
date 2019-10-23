#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Example command to use apktool
#docker run --rm -v `pwd`:/appA 

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io

#Define jadx  version
ENV JADX_VERSION=1.0.0
RUN apk add --no-cache wget unzip

#Change workdir
WORKDIR /usr/local/bin

# Download and Install jd-cmd
RUN wget -q -O "jadx.zip" "https://github.com/skylot/jadx/releases/download/v1.0.0/jadx-$JADX_VERSION.zip"
RUN unzip -q "jadx.zip" -d ./tools
RUN chmod +x "./tools/bin/jadx"

VOLUME ["/data"]

WORKDIR /data

ENTRYPOINT ["/usr/local/bin/tools/bin/jadx"]

CMD ["--help"]

