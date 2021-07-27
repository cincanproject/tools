FROM debian:10-slim as env

LABEL MAINTAINER=cincan.io

ARG tool_version=93e36e8f049a15666146eb508c96e785f3861493
ENV TOOL_VERSION=$tool_version

ENV DEBIAN_FRONTEND=noninteractive

# Opt out of Microsoft telemetry
ENV POWERSHELL_TELEMETRY_OPTOUT=1

# Dependencies for PowerShell and box-ps
RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    wget \
    less \
    locales \
    ca-certificates \
    gss-ntlmssp \
    unzip \
    && \
    wget -q https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y powershell && \
    apt-get dist-upgrade -y && \
    locale-gen $LANG && \
    update-locale  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    wget -q -O "box-ps.zip" "https://github.com/ConnorShride/box-ps/archive/$TOOL_VERSION.zip" && \
    unzip -q box-ps.zip && \
    rm box-ps.zip && \
    mv box-ps-$TOOL_VERSION /opt/box-ps && \
    adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    install -d -o appuser -g appuser /home/appuser/tool

USER appuser
WORKDIR /home/appuser/tool

COPY meta.json /opt/

ENTRYPOINT ["pwsh", "/opt/box-ps/box-ps.ps1"]
