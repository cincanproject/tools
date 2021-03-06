# Modified from https://github.com/blacktop/docker-ghidra
ARG tool_version=ghidra_9.2.2_PUBLIC_20201229

FROM openjdk:11-jdk-slim as build

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV GHIDRA_SHA256 8cf8806dd5b8b7c7826f04fad8b86fc7e07ea380eae497f3035f8c974de72cf8

RUN apt-get update && apt-get install -y wget ca-certificates unzip --no-install-recommends \
    && wget --progress=bar:force -O /tmp/ghidra.zip https://ghidra-sre.org/$TOOL_VERSION.zip \
    && echo "$GHIDRA_SHA256 /tmp/ghidra.zip" | sha256sum -c - \
    && unzip /tmp/ghidra.zip \
    && mv $(echo ${TOOL_VERSION} | cut -f1-3 -d"_") /ghidra \
    && chmod +x /ghidra/ghidraRun  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/* /ghidra/docs /ghidra/Extensions/Eclipse /ghidra/licenses


# Make multi-stage build, use jre instead of jdk here, wit h Eclipse OpenJ9
FROM adoptopenjdk:11-jdk-openj9-bionic as runtime

ARG tool_version
ENV TOOL_VERSION=$tool_version

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
    && apt-get update && apt-get install -y libxml2-utils \
    && echo "===> Clean up unnecessary files..." \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*


COPY ghidra_decompiler.sh /ghidra
RUN chmod +x /ghidra/ghidra_decompiler.sh

RUN chown -R appuser:appuser /ghidra

USER appuser
WORKDIR /home/appuser/

COPY .cincanignore .

# Define ghidra location for script, it is expecting $GHIDRA_HOME variable
ENV GHIDRA_HOME /ghidra

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["/ghidra/ghidra_decompiler.sh" ]
CMD ["--help"]
