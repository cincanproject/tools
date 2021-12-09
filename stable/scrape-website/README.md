# "Headless Chromium web browser"

Headless Chromium browser to screenshot URLs and save the navigation generated traffic as a HAR file

## Input

```
url, json
```

## Output

```
png, har (json)
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*scrape-website/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/scrape-website/Dockerfile))

## Usage

Screenshot an URL to png with the `cincan` (https://gitlab.com/cincan/cincan-command) tool:
```
cincan run cincan/scrape-website --url https://example.com --png -o screenshots
```

or using `docker` directly

```
docker run --rm -v $PWD/screenshots:/screenshots cincan/scrape-website --url http://example.com --png -o /screenshots
```

Collect HAR (HTTP Archive) file of the browser interaction with an url
```
cincan run cincan/scrape-website --url https://example.com --har -o screenshots
```

HAR files are json, so you can query the file for example with [`jq`](https://stedolan.github.io/jq/).
How to get the content of all of the requests with `jq`:

```
jq .log.entries[].response.content.text <HAR file>
```

## Project homepage

[Google Chrome Puppeteer](https://github.com/GoogleChrome/puppeteer)
[chrome-har-capturer](https://github.com/cyrus-and/chrome-har-capturer)

