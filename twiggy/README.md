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
docker run -v /samples:/samples cincan/twiggy <OPTIONS> /samples/sample.wasm
```

***Options***  

```
-h, --help    :Prints help information
-V, --version :Prints version information
diff          :Diff the old and new versions of a binary to see what sizes changed.
dominators    :Compute and display the dominator tree for a binary's call graph.
garbage       :Find and display code and data that is not transitively referenced by any exports or public
              functions.
help          :Prints this message or the help of the given subcommand(s)
monos         :List the generic function monomorphizations that are contributing to code bloat.
paths         :Find and display the call paths to a function in the given binary's call graph.
top           :List the top code size offenders in a binary.
```


## Project homepage

https://github.com/rustwasm/twiggy
