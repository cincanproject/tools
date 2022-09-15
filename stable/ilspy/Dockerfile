# Ilspycmd, decompiler of .net code https://www.nuget.org/packages/ilspycmd/
# Source: https://github.com/icsharpcode/ILSpy

# Currently uses  .NET Core SDK 2.2 with Debian Stretch
# Note: problems with Alpine base: help not printed correctly due to paging

# Example:
# docker run -v /samples:/samples cincan/ilspy /samples/ilspysample.exe

ARG tool_version=7.2.1.6856
FROM mcr.microsoft.com/dotnet/sdk:3.1-bullseye AS build

ARG tool_version
ENV TOOL_VERSION=$tool_version

LABEL MAINTAINER=cincan.io

RUN dotnet tool  install --no-cache  ilspycmd --tool-path /usr/local/bin/ --version $TOOL_VERSION

FROM mcr.microsoft.com/dotnet/runtime:3.1-bullseye-slim

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /usr/local/bin /usr/local/bin
RUN   groupadd -g 1000 appuser \
   && useradd -u 1000 -g appuser -s /sbin/nologin appuser \
   && chmod +x /usr/local/bin/ilspycmd

USER appuser
WORKDIR "/home/appuser"

COPY meta.json /opt/

ENTRYPOINT ["/usr/local/bin/ilspycmd"]
CMD ["--help"]
