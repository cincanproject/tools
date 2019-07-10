# Extracts urls, hashes (md5, sha1, sha256, sha512), emails and ips from a file
# Writes results in seperate directories under given output directory
# Results are in newline delimited text file
#
# build:
# docker build -t cincan/iocextract .
#
# usage example 1 loads all files from /files/ and extracts hashes:
# docker run -v /files:/files cincan/iocextract --output /files/output/ --path /files/ --hash
# usage example 2 loads specific file from mounted volume and exracts emails, urls
# docker run -v /files:/files cincan/iocextract --output /files/output/ --path /files/file -u -e
#
# [options]
# [--verbose, -v] Sets verbosity to high, prints lists of found urls and hashes
# [--url, -u] Extracts urls
# [--hash] Extracts hashes (md5, sha1, sha256, sha512)
# [--email, -e] Extracts emails
# [--ip, -i] Extracts ips (ipv4, ipv6)

FROM python:3.6-alpine
RUN apk update \
    && apk add --no-cache alpine-sdk python-dev \
    && pip install iocextract
COPY /iocextract .
ENTRYPOINT ["python", "extract.py"]

