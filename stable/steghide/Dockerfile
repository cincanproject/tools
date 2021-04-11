ARG tool_version=0.5.1-13

FROM debian:10-slim

LABEL MAINTAINER=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt update && apt install --no-install-recommends -y \
        steghide=$TOOL_VERSION \
        && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser

USER appuser

WORKDIR /home/appuser

# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["steghide"]
CMD ["--help"]
