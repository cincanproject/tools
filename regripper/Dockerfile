ARG tool_version=1b87d069e4a79e4a6e8940492527f10bb2b91840
FROM debian:10-slim as build

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       git \
       ca-certificates

# TODO: wait for upstream to support alternative plugins dir
RUN git clone --depth=1 https://github.com/keydet89/RegRipper2.8.git /regripper \
    && cd /regripper \
    && git checkout $REGRIPPER_VERSION \
    && sed -i 's_#my $plugindir_my $plugindir_g' rip.pl \
    && sed -i 's_#push_push_' rip.pl \
    && sed -i 's_"plugins/";_"/regripper/plugins/";_' rip.pl \
    && sed -i 's_("plugins");_("/regripper/plugins");_' rip.pl

FROM debian:10-slim as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

ENV PERL5LIB=/regripper
COPY --from=build /regripper/rip.pl /regripper/
COPY --from=build /regripper/plugins /regripper/plugins

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libparse-win32registry-perl && \
    rm -rf /var/lib/apt/lists/* && \
    adduser --shell /sbin/nologin --disabled-login --gecos "" appuser && \
    mkdir /home/appuser/tool

USER appuser
WORKDIR /home/appuser/tool

ENTRYPOINT ["perl", "/regripper/rip.pl"]
