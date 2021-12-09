#!/usr/bin/env node
'use strict';

const puppeteer = require('puppeteer');
const CHC = require('chrome-har-capturer');
const url = require('url');
const fs = require('fs');
const { promisify } = require('util');

var ArgumentParser = require('argparse').ArgumentParser;
var parser = new ArgumentParser({
  version: '1.1',
  addHelp: true,
  description: 'Open URL with a browser'
});

parser.addArgument([ '--delay' ], {
  help: 'How many milliseconds to wait after opening the url',
  type: 'int',
});

parser.addArgument([ '--process-timeout' ], {
  help: 'How long to wait until Chromium should be killed',
  type: 'int',
  defaultValue: 30000,
});

parser.addArgument([ '--resolution' ], {
  help: 'Resolution of the screenshot, default is 1366x768',
  defaultValue: "1366x768"
});

parser.addArgument([ '--output-har', '--har' ], {
  help: 'Output HTTP Archive file(s)',
  action: 'storeTrue'
});

parser.addArgument([ '--output-png', '--png' ], {
  help: 'Output a png screenshot of the URL(s)',
  action: 'storeTrue'
});

parser.addArgument([ '--url' ], {
  help: 'Single url to scrape'
});

parser.addArgument([ '--url-file' ], {
  help: 'JSON file to read urls from, example: { "url_list": [ "http://example.com", "..." ] }'
});

parser.addArgument([ '-o', '--output-dir' ], {
  help: 'Directory to output files to, default is CWD',
  defaultValue: "."
});

parser.addArgument([ '--user-agent' ], {
  help: 'User-agent of the browser',
  defaultValue: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
});

parser.addArgument([ '--chromium-args' ], {
  help: 'Arguments to pass on to the Chromium process'
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

if (!(args.url_file || args.url)) {
    parser.error("Give --url or --url-file as argument")
    parser.printHelp();
    process.exit(1);
}

if (!args.output_har && !args.output_png) {
    args.output_har = true;
    args.output_png = true;
}

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

async function finish(url, events, har_path) {
    try {
        // Ignore "Incomplete event log" errors from library
        const har = await CHC.fromLog(url, events, { content: true }).catch(e => {});
        await promisify(fs.writeFile)(har_path, JSON.stringify(har));
    } catch (e) {
        console.error(e.message);
    }
}

process.on('uncaughtException', (error) => {
    console.error(error);
    process.exit(1);
});

process.on('unhandledRejection', (reason, p) => {
    console.error(reason, p);
    process.exit(1);
});

if (args.output_dir) {
    if (!fs.existsSync(args.output_dir)){
        fs.mkdirSync(args.output_dir);
    }
}

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
    let dateStr = now.toISOString().replace(/:/g, '_');
    let [width, height] = args.resolution.split('x').map(v => parseInt(v, 10));
    let delay = parseInt(args.delay, 10);

    const http_uri_scheme = new RegExp("^[a-z]+://")

    if (!http_uri_scheme.test(scrape_url)) {
        console.log("No URI Scheme supplied, assuming https://");
        scrape_url = "https://" + scrape_url
    }

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

    page.setViewport({
        width,
        height
    });

    page.setUserAgent(args.user_agent);

    const client = await page.target().createCDPSession();
    if (args.output_har) {
        // Code borrowed from issue:
        // https://github.com/cyrus-and/chrome-har-capturer/issues/75

        let counter = 0;
        let events = [];

        const watchedEvents = [
            'Network.dataReceived',
            'Network.loadingFailed',
            'Network.loadingFinished',
            'Network.requestWillBeSent',
            'Network.resourceChangedPriority',
            'Network.responseReceived',
            'Page.domContentEventFired',
            'Page.loadEventFired'
        ];

        await client.send('Page.enable');
        await client.send('Network.enable');

        watchedEvents.forEach(method => {
            client.on(method, params => {
                events.push({method, params});
            });
        });

        const har_path = `${args.output_dir}/${hostname}_${dateStr}.har`;
        stdout['har_output'] = har_path

        client.on('Network.loadingFinished', async ({requestId}) => {
            // call Network.getResponsebody manually for each
            // Network.loadingFinished events
            counter++;
            const params = await client.send('Network.getResponseBody', {requestId});
            counter--;

            // build the synthetic events
            const {body, base64Encoded} = params;
            events.push({
                method: 'Network.getResponseBody',
                params: {
                    requestId,
                    body,
                    base64Encoded
                }
            });

            // when there are no more pending invocations build the HAR
            if (counter === 0) {
                finish(scrape_url, events, har_path)
            }
        });
    }

    try {
        await page.goto(scrape_url, {waitUntil: 'networkidle0'});
        await sleep(delay);
    } catch (e) {
        clearTimeout(browserTimeout);
        stdout['logs'] = String(e);
        await browser.close();
        console.log(JSON.stringify(stdout));
        return
    }

    if (args.output_png) {
        let png = `${args.output_dir}/${hostname}_${width}_${height}_${dateStr}.png`;
        await page.screenshot({path: `${png}`, fullPage: true});
        stdout['png_output'] = png
    }

    await client.detach();
    await browser.close();
    clearTimeout(browserTimeout);

    console.log(JSON.stringify(stdout));
}
