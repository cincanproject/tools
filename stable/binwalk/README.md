# Firmware Analysis Tool

Binwalk with some optional run-time dependencies.

## Supported tags and respective `Dockerfile` links

* `latest` 
([*binwalk/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/binwalk/Dockerfile))

## Input

```
binary
```

## Output

```
Binwalk report
```

## Usage

***Binwalk help***

`$ docker run cincan/binwalk --help`

***Binwalk basic usage for identifying embedded data***

`$ docker run -v $PWD/samples:/samples cincan/binwalk /samples/firmware.bin`

***Usage with cincan cli tool to extract embedded compressed data blocks***
`$ cincan run cincan/binwalk -v -Me ../_samples/compressed/tampered_sample.bin -C sample-output/`

## Project homepage

https://github.com/ReFirmLabs/binwalk

## License

MIT License

