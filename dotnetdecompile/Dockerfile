# Ilspy, decompiler of .net code https://www.nuget.org/packages/ilspycmd/
# docker run -v /samples:/samples cincan/dotnetdecompile /samples/dotnetsample.exe

FROM ubuntu:16.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-transport-https \
    wget \
    ca-certificates \
    && wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install --no-install-recommends -y dotnet-sdk-2.2

ARG DOTNET_CLI_TELEMETRY_OPTOUT=true

RUN dotnet tool  install --no-cache  ilspycmd --tool-path /usr/local/bin/ \
    && adduser --shell /sbin/nologin --disabled-login --gecos "" appuser \
    && apt-get --purge remove -y wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

USER appuser

ENTRYPOINT ["/usr/local/bin/ilspycmd"]
CMD ["--help"]
