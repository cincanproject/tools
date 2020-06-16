# "Headless Thunderbird to screenshot email messages"

Headless thunderbird to screenshot `.eml` files

You can find an example `.eml` dataset here: https://github.com/warmspringwinds/email_spam_filtering

## Input

```
eml
```

## Output

```
png
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*headless-thunderbird/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/headless-thunderbird/Dockerfile))

## Usage

Screenshot an `.eml` file content to file `output/mail.eml.png`

`cincan` (https://gitlab.com/cincan/cincan-command) tool:
```
cincan run cincan/headless-thunderbird -f mail.eml -s 800x1000 -o output
```

or using `docker` directly, the sample in absolute directory <SAMPLES>
(e.g. `/home/user/maildata/`)

```
docker run --rm -v <SAMPLES>:/maildata cincan/headless-thunderbird -f /maildata/mail.eml -s 800x1000 -o output
```

## Project homepage

[Thunderbird home page](https://www.thunderbird.net)
