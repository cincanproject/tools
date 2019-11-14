# Ilspycmd, decompiler of .net code https://www.nuget.org/packages/ilspycmd/
# Source: https://github.com/icsharpcode/ILSpy

# Currently uses  .NET Core SDK 2.2 with Debian Streatch
# Note: problems with Alpine base: help not printed correctly due to paging

# Example:
# docker run -v /samples:/samples cincan/ilspy /samples/ilspysample.exe

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch

ENV VERSION=5.0.2

LABEL MAINTAINER=cincan.io

RUN dotnet tool  install --no-cache  ilspycmd --tool-path /usr/local/bin/ --version $VERSION \
    && groupadd -g 1000 app \
    && useradd -u 1000 -G app -s /sbin/nologin appuser \
    # Alpine base alterinatives
    #&& addgroup -S app \
    #&& adduser -s /sbin/nologin --disabled-password -g "" appuser app \
    && chmod +x /usr/local/bin/ilspycmd

USER appuser

ENTRYPOINT ["/usr/local/bin/ilspycmd"]
CMD ["--help"]
