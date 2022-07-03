#Analyzes Android apk files using apktool 
ARG tool_version=2.6.0
ARG tool_sha256=f750a3cd2c1f942f27f5f7fd5d17eada3bdaff0a6643f49db847e842579fdda5
#Java 1.8 is required
FROM openjdk:8-jre-alpine as build

ARG tool_version
ARG tool_sha256

LABEL MAINTAINER=cincan.io

ENV TOOL_VERSION=${tool_version}
ENV TOOL_SHA256=${tool_sha256}

RUN apk add --no-cache curl bash \
    && addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

USER appuser
WORKDIR /home/appuser/

# Check integrity of external script file as well
ENV SCRIPT_SHA256=e9a49351b4df65d532e7c3cef27144c7e0e1c2daad1e367e65b2acef6715b863
RUN curl -sLO https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool \
    && echo "${SCRIPT_SHA256}  apktool" \
    && curl -sLO https://github.com/iBotPeaches/Apktool/releases/download/v${TOOL_VERSION}/apktool_${TOOL_VERSION}.jar  && echo "${TOOL_SHA256}  apktool_${TOOL_VERSION}.jar" | sha256sum -c \
    && mv apktool_${TOOL_VERSION}.jar apktool.jar && chmod +x apktool.jar

FROM openjdk:8-jre-alpine as runtime

arg tool_version
ENV TOOL_VERSION=${tool_version}

RUN addgroup -S appuser && \
    adduser -s /sbin/nologin --disabled-password -G appuser appuser

USER appuser
WORKDIR /home/appuser/tool

COPY --from=build /home/appuser/apktool /home/appuser/apktool.jar /home/appuser/tool/
COPY meta.json /opt/

ENTRYPOINT ["sh", "/home/appuser/tool/apktool"]
