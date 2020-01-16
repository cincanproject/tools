# "TruffleHog Searches through git repositories for accidentally committed secrets"

## Input

```
git repository
```

## Output

```
trufflehog report (JSON option)
```

## Supported tags and respective `Dockerfile` links
* `latest` 
([*truffleHog/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/trufflehog/Dockerfile))

## Usage

`$ docker run -v /samples:/samples cincan/trufflehog file:///samples/<GIT-DIR>/ 
<OPTIONS>`

***or*** 

`$ docker run cincan/trufflehog https://github.com/<USERNAME>/sample.git <OPTIONS>`

Some options:
```
--json        Output in JSON
--regex       High signal regex checks
```

## Project homepage

https://github.com/dxa4481/truffleHog
