# TruffleHog
Searches through git repositories for accidentally committed secrets!

## Build:
```
docker build -t cincan/trufflehog .
```

## Usage:
```
docker run -v /samples:/samples cincan/trufflehog file:///samples/<GIT-DIR>/ <OPTIONS>
```

or

```
docker run cincan/trufflehog https://github.com/<USERNAME>/sample.git <OPTIONS>
```

### Some <OPTIONS>:
```
--json        Output in JSON
--regex       High signal regex checks
```
