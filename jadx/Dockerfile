#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io

#Define jadx  version
ENV VERSION=1.0.0
RUN apk add --no-cache wget unzip

# Add an user
RUN mkdir -p /home/appuser \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

#change user and workdir
USER appuser
WORKDIR /home/appuser

# Download and Install jd-cmd
RUN wget -q -O "jadx.zip" "https://github.com/skylot/jadx/releases/download/v1.0.0/jadx-$VERSION.zip"
RUN unzip -q "jadx.zip" -d ./tools
RUN chmod +x "./tools/bin/jadx"

ENTRYPOINT ["/home/appuser/tools/bin/jadx"]

