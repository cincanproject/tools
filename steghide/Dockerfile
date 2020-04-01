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

ENTRYPOINT ["steghide"]
CMD ["--help"]
