# TruffleHog Searches through git repositories for accidentally committed secrets

## Input

```
git repository
```

## Output

```
trufflehog report, JSON
```

## Supported tags and respective `Dockerfile` links
* `latest` 
([*truffleHog/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/trufflehog/Dockerfile))

## Usage

Using with cincan-command, input and output files are handled automatically into container:

```console
cincan run cincan/trufflehog <url-or-path/to/git/sample.git>
```

```console
cincan run cincan/trufflehog https://gitlab.com/CinCan/tools.git

```
Or use with Docker, requires the usage of volumes:

```
docker run -v /samples:/samples cincan/trufflehog file:///samples/<GIT-DIR>/ 
<OPTIONS>
```

***or*** just using remote repository

```
docker run cincan/trufflehog https://github.com/<USERNAME>/sample.git <OPTIONS>
```

Some options:
```
--json        Output in JSON
--regex       High signal regex checks
```

See project home page for all available options.


## Project homepage

https://github.com/dxa4481/truffleHog


## License 

Apache 2.0