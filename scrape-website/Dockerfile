FROM node:11.12.0-alpine

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/ \
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true" \
    NODE_PATH="/usr/local/share/.config/yarn/global/node_modules:${NODE_PATH}"

RUN apk add --no-cache \
    chromium \
    harfbuzz \
    nss \
    && yarn add puppeteer@1.14.0 \
    && yarn add argparse@1.0.10 \
    && yarn add puppeteer-har@1.0.6 \
    && yarn cache clean \
    && rm -rf /var/cache/* \
    && mkdir /var/cache/apk

# Add chrome user
RUN mkdir -p /chrome \
    && adduser -D chrome \
    && chown -R chrome:chrome /chrome

USER chrome
WORKDIR /chrome

ADD "scrape-website.js" .
ENTRYPOINT ["node", "scrape-website.js"]
