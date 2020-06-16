FROM debian:10-slim as build

ENV TOOL_VERSION=ee874d5245fb4f26147c29dc1db02b8e68a88698

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

ENV TOOL_VERSION=ee874d5245fb4f26147c29dc1db02b8e68a88698

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
