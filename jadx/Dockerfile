#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

#Java 1.8 is needed
FROM openjdk:8-alpine

LABEL MAINTAINER=cincan.io

#Define jadx  version
ENV VERSION=1.1.0
RUN apk add --no-cache wget unzip

ENV JADX_SHA256 91948067a60feee36512e043b288f726678ddd760aa11a01496b53df95465b16

# Add an user
RUN mkdir -p /home/appuser/tool \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

#change user and workdir
USER appuser
WORKDIR /home/appuser/tool

# Download and Install jadx
RUN wget -q -O "jadx-${VERSION}.zip" "https://github.com/skylot/jadx/releases/download/v$VERSION/jadx-$VERSION.zip"
RUN echo "${JADX_SHA256}  jadx-${VERSION}.zip"| sha256sum -c -

RUN unzip -q "jadx-${VERSION}.zip"
RUN chmod +x "./bin/jadx"

ENTRYPOINT ["./bin/jadx"]
