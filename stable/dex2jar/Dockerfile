#Dex files to jar
#Example command to use dex2jar tool with docker
#docker run --rm -v `pwd`:/samples dex2jar path/to/your/.apk
ARG tool_version=2.1
#Base image
FROM openjdk:8-jre-alpine

ARG tool_version
LABEL MAINTAINER=cincan.io

#Define apktool version
ENV TOOL_VERSION=${tool_version}
#add needed tools
RUN apk add --no-cache wget unzip \
    && mkdir -p /home/appuser \
    && adduser -D appuser \
    && chown -R appuser:appuser /home/appuser

WORKDIR /home/appuser

#Download dex2jar tool, unzip it and give it right permissions
RUN wget -q -O "dex-tools.zip" "https://github.com/pxb1988/dex2jar/files/1867564/dex-tools-$TOOL_VERSION-SNAPSHOT.zip" \
    && unzip -q "dex-tools.zip" -d . \
    && chmod +x ./dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh \
    && apk del unzip wget

USER appuser

COPY meta.json /opt/

ENTRYPOINT ["/home/appuser/dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh"]
