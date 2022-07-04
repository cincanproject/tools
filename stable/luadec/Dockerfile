ARG tool_version=895d92313fabaee260121c758c8320d1b21dd741

FROM debian:10-slim as build
ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ make cmake liblua5.3-dev git ca-certificates libreadline-dev && \
    git clone --depth=1 https://github.com/viruscamp/luadec && \
    cd luadec && \
    git checkout -b build $TOOL_VERSION && \
    git submodule update --init lua-5.1 && \
    cd lua-5.1 && \
    make linux && \
    cd ../luadec && \
    make LUAVER=5.1

FROM gcr.io/distroless/base-debian10 as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /luadec/luadec/luadec /usr/local/bin/
COPY --from=build /luadec/luadec/luaopswap /usr/local/bin/
COPY --from=build /luadec/luadec/luareplace /usr/local/bin/

USER nonroot
WORKDIR /home/nonroot/tool

# Keep metafile as final modification for layers! Easily fetchable in that case
COPY meta.json /opt/

ENTRYPOINT ["/usr/local/bin/luadec"]
