# Command line port of 7-Zip which provides utilities to (un)pack compressed archives

## Input

```
7z, ZIP, GZIP, BZIP2, XZ, TAR, APM, ARJ,
CAB, CHM, CPIO, CramFS, DEB, DMG, FAT,
HFS, ISO, LZH, LZMA, LZMA2, MBR, MSI,
MSLZ, NSIS, NTFS, RAR, RPM, SquashFS,
UDF,VHD, WIM, XAR, Z
```

## Output

```
data, 7z, ZIP, GZIP, BZIP2, XZ, TAR
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*7zip/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/stable/7zip/Dockerfile))

## Usage

### Extract archive

Extract all paths from an archive file with the [`cincan`](https://gitlab.com/cincan/cincan-command) tool:

```
cincan run cincan/7zip x sample.zip
```

or using `docker` directly, the sample in absolute directory <SAMPLES>
(e.g. `/home/myname/mysamples`)

```
docker run --rm -v <SAMPLES>:/samples cincan/7zip x sample.zip
```

## Project homepage

https://sourceforge.net/projects/p7zip/
