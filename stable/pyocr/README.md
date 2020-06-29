# Optical character recognition (OCR) wrapper for Tesseract OCR engine

## Input

```
PDF, png, jpg
```

## Output

```
text data
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*pyocr/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/pyocr/Dockerfile))

## Usage

### Extract text

Extract text from a PNG image with the [`cincan`](https://gitlab.com/cincan/cincan-command) tool:

```
cincan run cincan/pyocr samples/scam-sms.png
```

or using `docker` directly, the sample in absolute directory <SAMPLES>
(e.g. `/home/myname/mysamples`)

```
docker run --rm -v <SAMPLES>:/samples cincan/pyocr /samples/scam-sms.png
```

### OCR only digits

You can OCR only digits (phone numbers) with the `-d` flag:

```
cincan run cincan/pyocr samples/scam-sms.png -d
```

Using `docker` directly

```
docker run --rm -v <SAMPLES>:/samples cincan/pyocr /samples/scam-sms.png -d
```

## Project homepage

https://gitlab.gnome.org/World/OpenPaperwork/pyocr
