# Extract data from Windows registry

RegRipper CLI (`rip.pl`) can be used to read data out of Windows registry hives with plugins.
Written by [Harlan 'keydet89' Carvey](https://windowsir.blogspot.com/).

## Input

```
Windows registry hive files
```

## Output

```
report data
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*regripper/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/regripper/Dockerfile))

## Usage

To see what plugins are supported by regripper, run the `-l` option with the
[`cincan`](https://gitlab.com/CinCan/cincan-command) tool:

```
cincan run cincan/regripper -l
```

Extract Run and RunOnce keys from registry (commands that run every time a user logs on) with `docker`

```
docker run --rm -v `pwd`:/samples cincan/regripper -r /samples/SOFTWARE -p soft_run
```

Extract user and group information from the 'SAM' hive file with the `samparse` plugin:

```
cincan run cincan/regripper -r samples/SAM -p samparse
```

Extract installed applications

```
cincan run cincan/regripper -r samples/SOFTWARE -p product
```

Extract the exact Windows version of the registry

```
cincan run cincan/regripper -r samples/SOFTWARE -p winver
```

## Project homepage

[https://github.com/keydet89/RegRipper3.0](https://github.com/keydet89/RegRipper3.0)

