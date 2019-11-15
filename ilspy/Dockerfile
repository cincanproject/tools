# Ilspycmd, decompiler of .net code https://www.nuget.org/packages/ilspycmd/
# Source: https://github.com/icsharpcode/ILSpy

# Currently uses  .NET Core SDK 2.2 with Debian Stretch
# Note: problems with Alpine base: help not printed correctly due to paging

# Example:
# docker run -v /samples:/samples cincan/ilspy /samples/ilspysample.exe

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build

ENV VERSION=5.0.2

LABEL MAINTAINER=cincan.io

RUN dotnet tool  install --no-cache  ilspycmd --tool-path /usr/local/bin/ --version $VERSION

FROM mcr.microsoft.com/dotnet/core/runtime:2.1
COPY --from=build /usr/local/bin /usr/local/bin
RUN   groupadd -g 1000 app \
   && useradd -u 1000 -G app -s /sbin/nologin appuser \
   && chmod +x /usr/local/bin/ilspycmd

USER appuser
WORKDIR "/home/appuser"

ENTRYPOINT ["/usr/local/bin/ilspycmd"]
CMD ["--help"]
