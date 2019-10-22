# Modified from https://github.com/blacktop/docker-ghidra
FROM openjdk:11-jdk-slim

LABEL MAINTAINER=cincan.io

ENV VERSION 9.1-BETA_DEV
ENV GHIDRA_SHA 3d61de711b7ea18bdee3ed94c31429e4946603b3e7d082cca5e949bbd651f051 

RUN apt-get update && apt-get install -y wget ca-certificates unzip --no-install-recommends \
    && wget --progress=bar:force -O /tmp/ghidra.zip https://ghidra-sre.org/ghidra_9.1-BETA_DEV_20190923.zip \
    && echo "$GHIDRA_SHA /tmp/ghidra.zip" | sha256sum -c - \
    && unzip /tmp/ghidra.zip \
    && mv ghidra_${VERSION} /ghidra \
    && chmod +x /ghidra/ghidraRun \
    && echo "===> Clean up unnecessary files..." \
    && apt-get purge -y --auto-remove wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* /ghidra/docs /ghidra/Extensions/Eclipse /ghidra/licenses

WORKDIR /ghidra
RUN mkdir /ghidra/projects/
COPY DecompileHeadless.java /ghidra/Ghidra/Features/Decompiler/ghidra_scripts/
COPY loggings.tgz /ghidra/support/


# Disable illegal reflective access warnings to just produce decompiled code

RUN sed -i '/VMARG_LIST+="-XX:CICompilerCount=2 "/a VMARG_LIST+="--add-opens java.base/java.lang=ALL-UNNAMED"' /ghidra/support/analyzeHeadless

RUN tar -C /ghidra/support -zxvf /ghidra/support/loggings.tgz  \
     && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser


RUN chown -R appuser:appuser /ghidra

USER appuser

ENTRYPOINT ["/ghidra/support/analyzeHeadless", "/ghidra/projects/", "ANewProject", "-postScript", "DecompileHeadless.java", "-readOnly", "-import" ]
