ARG tool_version=05ef95773b2b417d0a3e14382f6002c0a57db6c3
FROM debian:10-slim as build

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       git \
       ca-certificates

# TODO: wait for upstream to support alternative plugins dir
RUN git clone --depth=1 https://github.com/keydet89/RegRipper3.0.git /regripper \
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
# meta.json should be kept as final modification for layers
COPY meta.json /opt/
ENTRYPOINT ["perl", "/regripper/rip.pl"]
