# Twiggy 
analyzes a binary's call graph: Why was the function included in the  binary, what is the retained size of a function

Twiggy currently supports  WebAssembly's .wasm format. (Partial support:  ELF, Mach-O)

## Build:
```
docker build -t cincan/twiggy .
```
## Usage:
```
docker run -v /samples:/samples cincan/twiggy <TWIGGY-SUBCOMMAND> /samples/sample.wasm
```

```
<TWIGGY-SUBCOMMAND> = dominators/garbage/help/monos/paths/top/diff(requires /oldversion.wasm /newversion.wasm)
```
