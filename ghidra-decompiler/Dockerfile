# Modified from https://github.com/blacktop/docker-ghidra
FROM openjdk:11-jdk-slim as build

LABEL MAINTAINER=cincan.io

ENV VERSION 9.1_PUBLIC
ENV GHIDRA_SHA256 29d130dfe85da6ec45dfbf68a344506a8fdcc7cfe7f64a3e7ffb210052d1875e 

RUN apt-get update && apt-get install -y wget ca-certificates unzip --no-install-recommends \
    && wget --progress=bar:force -O /tmp/ghidra.zip https://ghidra-sre.org/ghidra_9.1_PUBLIC_20191023.zip \
    && echo "$GHIDRA_SHA256 /tmp/ghidra.zip" | sha256sum -c - \
    && unzip /tmp/ghidra.zip \
    && mv ghidra_${VERSION} /ghidra \
    && chmod +x /ghidra/ghidraRun  \
    # && rm -rf /ghidra/docs /ghidra/Extensions/Eclipse /ghidra/licenses
#    && echo "===> Clean up unnecessary files..." \
#    && apt-get purge -y --auto-remove wget \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* /ghidra/docs /ghidra/Extensions/Eclipse /ghidra/licenses


# Make multi-stage build, use jre instead of jdk here, wit h Eclipse OpenJ9
FROM adoptopenjdk:11-jre-openj9 as runtime

WORKDIR /ghidra

COPY --from=build /ghidra /ghidra

RUN mkdir /ghidra/projects/

RUN du -sh /ghidra

COPY DecompileHeadless.java /ghidra/Ghidra/Features/Decompiler/ghidra_scripts/
COPY loggings.tgz /ghidra/support/


# Disable illegal reflective access warnings to just produce decompiled code

RUN sed -i '/VMARG_LIST+="-XX:CICompilerCount=2 "/a VMARG_LIST+="--add-opens java.base/java.lang=ALL-UNNAMED"' /ghidra/support/analyzeHeadless

RUN tar -C /ghidra/support -zxvf /ghidra/support/loggings.tgz  \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && echo "===> Clean up unnecessary files..." \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*


RUN chown -R appuser:appuser /ghidra

USER appuser
WORKDIR /home/appuser/

ENTRYPOINT ["/ghidra/support/analyzeHeadless", "/ghidra/projects/", "ANewProject", "-postScript", "DecompileHeadless.java", "-readOnly", "-import" ]
