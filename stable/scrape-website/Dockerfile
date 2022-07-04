ARG tool_version=1.3

FROM node:alpine as build
ARG tool_version
ENV TOOL_VERSION=$tool_version

RUN apk add --no-cache git \
    && git clone --branch=master https://gitlab.com/CinCan/scrape-website \
    && yarn add --frozen-lockfile ./scrape-website \
    && yarn cache clean

FROM node:alpine as env

ARG tool_version
ENV TOOL_VERSION=$tool_version

COPY --from=build /node_modules /node_modules
COPY --from=build /scrape-website/scrape-website.js /

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true"

RUN apk add --no-cache chromium tcpdump libcap \
    && deluser --remove-home node \
    && adduser -D appuser \
    && addgroup pcap \
    && addgroup appuser pcap \
    && chgrp pcap /usr/bin/tcpdump \
    && chmod 750 /usr/bin/tcpdump \
    && setcap cap_net_raw,cap_net_admin=eip /usr/bin/tcpdump \
    && mkdir -p /home/appuser/tool \
    && chown -R appuser:appuser /home/appuser

USER appuser
WORKDIR /home/appuser/tool

ENTRYPOINT ["node", "/scrape-website.js"]
