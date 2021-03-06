#!/usr/bin/env node
'use strict';

const puppeteer = require('puppeteer');
const PuppeteerHar = require('puppeteer-har');
const url = require('url');
const fs = require('fs');

var ArgumentParser = require('argparse').ArgumentParser;
var parser = new ArgumentParser({
  version: '1.0',
  addHelp: true,
  description: 'Open URL with a browser'
});

parser.addArgument([ '--delay' ], {
  type: 'int',
  defaultValue: 5,
});

parser.addArgument([ '--process-timeout' ], {
  type: 'int',
  defaultValue: 30000,
});

parser.addArgument([ '--resolution' ], {
  defaultValue: "1366x768"
});

parser.addArgument([ '--output-har' ], {
  action: 'storeTrue'
});

parser.addArgument([ '--output-png' ], {
  action: 'storeTrue'
});

parser.addArgument([ '--url' ], {
});

parser.addArgument([ '--url-file' ], {
});

parser.addArgument([ '--output-dir' ], {
  defaultValue: "."
});

parser.addArgument([ '--user-agent' ], {
  defaultValue: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
});

parser.addArgument([ '--chromium-args' ], {
});


var args = parser.parseArgs();

args.puppeteerOptions = {
  executablePath: process.env.CHROME_BIN || null,
  args: [
    '--no-sandbox',
    '--disable-setuid-sandbox'
  ],
  devtools: false,
  headless: true,
  ignoreHTTPSErrors: true,
  pipe: true, // TODO: does this help?
};


if (args.chromium_args) {
  args.puppeteerOptions.args = args.chromium_args.split(',');
}

function sleep(ms) {
    ms = (ms) ? ms : 0;
    return new Promise(resolve => {setTimeout(resolve, ms);});
}

function processTimeout(pid, ms, stdout) {
    ms = (ms) ? ms : 0;
    const err_logging = (stdout) => {
        try {
            process.kill(pid, 'SIGTERM');
        } catch (e) {
            stdout['logs'] = String(e);
        }
        console.log(JSON.stringify(stdout));
    }

    return setTimeout(err_logging, ms, stdout);
}

process.on('uncaughtException', (error) => {
    console.error(error);
    process.exit(1);
});

process.on('unhandledRejection', (reason, p) => {
    console.error(reason, p);
    process.exit(1);
});

if (args.url_file) {
    const metadata = JSON.parse(fs.readFileSync(args.url_file, 'utf8'));
    const url_list = metadata.url_list;
    for (let index = 0; index < url_list.length; ++index) {
        scrape(url_list[index], args);
    }
}

if (args.url) {
    scrape(args.url, args);
}

async function scrape(scrape_url, args) {
    let now = new Date();
    let dateStr = now.toISOString();
    let [width, height] = args.resolution.split('x').map(v => parseInt(v, 10));
    let delay = parseInt(args.delay, 10);
    let hostname = url.parse(scrape_url).hostname;

    let stdout = {
        url: scrape_url,
        date: dateStr,
        timestamp: Math.floor(now.getTime() / 1000),
        width: width,
        height: height
    };

    const browser = await puppeteer.launch({
        ...args.puppeteerOptions
    });

    const pid = browser.process().pid;
    const browserTimeout = processTimeout(pid, args.process_timeout, stdout);

    const page = await browser.newPage();
    const harsession = new PuppeteerHar(page);

    page.setViewport({
        width,
        height
    });

    page.setUserAgent(args.user_agent);

    await page.evaluateOnNewDocument(() => {
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false,
        });
    });

    if (args.output_har) {
        let har = `${hostname}_${dateStr}.har`;
        stdout['har_output'] = har
        await harsession.start({ path: `${args.output_dir}/${har}`, saveResponse: true });
    }

    try {
        await page.goto(scrape_url, {waitUntil: 'networkidle0'});
        await sleep(delay);
    } catch (e) {
        clearTimeout(browserTimeout);
        stdout['logs'] = String(e);
        browser.close();
        console.log(JSON.stringify(stdout));
        return
    }

    if (args.output_png) {
        let png = `${hostname}_${width}_${height}_${dateStr}.png`;
        await page.screenshot({path: `${args.output_dir}/${png}`, fullPage: true});
        stdout['png_output'] = png
    }

    if (args.output_har) {
        await harsession.stop();
    }

    browser.close();
    clearTimeout(browserTimeout);

    console.log(JSON.stringify(stdout));
}
