# Modified from https://github.com/blacktop/docker-ghidra
FROM openjdk:11-jdk-slim

ENV VERSION 9.0.2
ENV GHIDRA_SHA 10ffd65c266e9f5b631c8ed96786c41ef30e2de939c3c42770573bb3548f8e9f

RUN apt-get update && apt-get install -y wget ca-certificates unzip --no-install-recommends \
    && wget --progress=bar:force -O /tmp/ghidra.zip https://www.ghidra-sre.org/ghidra_9.0.2_PUBLIC_20190403.zip \
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
RUN tar -C /ghidra/support -zxvf /ghidra/support/loggings.tgz

ENTRYPOINT ["/ghidra/support/analyzeHeadless", "/ghidra/projects/", "ANewProject", "-postScript", "DecompileHeadless.java", "-readOnly", "-import", "2>/dev/null"]
