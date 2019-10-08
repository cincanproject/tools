FROM node:11.12.0-alpine

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/ \
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true" \
    NODE_PATH="/usr/local/share/.config/yarn/global/node_modules:${NODE_PATH}"

RUN apk add --no-cache \
    chromium>73.0.3683.103-r0 \
    harfbuzz \
    nss \
    && yarn add puppeteer@1.18.0 \
    && yarn add argparse@1.0.10 \
    && yarn add puppeteer-har@1.1.0 \
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
