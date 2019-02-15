# "Twiggy analyzes a binary's call graph"

## Input

```
.wasm, partial ELF & Mach-O support

```

## Output

```
twiggy report
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*twiggy/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/twiggy/Dockerfile))

## Usage
```
docker run -v /samples:/samples cincan/twiggy {{ TWIGGY-SUBCOMMAND }} /samples/sample.wasm
```

```
TWIGGY-SUBCOMMAND options: 

dominators
garbage
help
monos
paths
top
diff (requires /oldversion.wasm/newversion.wasm)
```

## Project homepage

https://github.com/rustwasm/twiggy