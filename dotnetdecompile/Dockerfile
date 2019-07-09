# Ilspycmd, decompiler of .net code https://www.nuget.org/packages/ilspycmd/
# docker run -v /samples:/samples cincan/dotnetdecompile /samples/dotnetsample.exe

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-alpine3.9

#RUN apk update && apk add install --no-cache \
#    wget=1.20.3-r0 \
#    ca-certificates=20190108-r0 \
#    && wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb \
#    && dpkg -i packages-microsoft-prod.deb \
#    && rm packages-microsoft-prod.deb \
#    && apt-get update \
#    && apt-get install --no-install-recommends -y dotnet-sdk-2.2

#ARG DOTNET_CLI_TELEMETRY_OPTOUT=true

RUN dotnet tool  install --no-cache  ilspycmd --tool-path /usr/local/bin/ \
    && addgroup -S app \
    && adduser -s /sbin/nologin --disabled-password -g "" appuser app \
    && chmod +x /usr/local/bin/ilspycmd
#    && apt-get --purge remove -y wget ca-certificates \
#    && rm -rf /var/lib/apt/lists/*

USER appuser

ENTRYPOINT ["/usr/local/bin/ilspycmd"]
CMD ["--help"]
