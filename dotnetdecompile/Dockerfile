# Ilspycmd, decompiler of .net code https://www.nuget.org/packages/ilspycmd/
# docker run -v /samples:/samples cincan/dotnetdecompile /samples/dotnetsample.exe

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-alpine3.9

LABEL MAINTAINER=cincan.io

RUN dotnet tool  install --no-cache  ilspycmd --tool-path /usr/local/bin/ \
    && addgroup -S app \
    && adduser -s /sbin/nologin --disabled-password -g "" appuser app \
    && chmod +x /usr/local/bin/ilspycmd

USER appuser

ENTRYPOINT ["/usr/local/bin/ilspycmd"]
CMD ["--help"]
