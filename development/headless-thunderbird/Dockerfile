ARG tool_version=1:68.7.0-1~deb10u1

FROM debian:10-slim

ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apt-get -y update \
    && apt-get install -y thunderbird=$TOOL_VERSION xvfb xdotool x11-apps imagemagick unzip zip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y

ENV XAUTHORITY=/root/.Xauthority

RUN touch /root/.Xauthority
COPY screenshot.sh /root/screenshot.sh
ADD thunderbird_profile.tar.gz /root/
RUN mkdir -p /root/tool

WORKDIR /root/tool

ENTRYPOINT ["bash", "/root/screenshot.sh"]
