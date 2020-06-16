#Analyzes Android apk files using apk tool and greps permission from AndroidManifest.xml file

ARG tool_version=1.1.0

#Java 1.8 is needed
FROM openjdk:8-jre-alpine

LABEL MAINTAINER=cincan.io

#Define jadx  version
ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV JADX_SHA256 91948067a60feee36512e043b288f726678ddd760aa11a01496b53df95465b16
RUN apk add --no-cache wget unzip \
    # Add an user
    && mkdir -p /home/appuser/tool \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

#change user and workdir
USER appuser
WORKDIR /home/appuser/tool

# Download and Install jadx
RUN wget -q -O "jadx-${TOOL_VERSION}.zip" "https://github.com/skylot/jadx/releases/download/v$TOOL_VERSION/jadx-$TOOL_VERSION.zip" \
    && echo "${JADX_SHA256}  jadx-${TOOL_VERSION}.zip"| sha256sum -c - \
    && unzip -q "jadx-${TOOL_VERSION}.zip" \
    && chmod +x "./bin/jadx" 

ENTRYPOINT ["./bin/jadx"]
