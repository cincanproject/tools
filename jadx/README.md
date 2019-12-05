# "Dex to Java decompiler"

## Input

```
.apk, .dex, .jar, .class, .smali, .zip, .aar, .arsc
```

## Output

```
Folder with decompiled .jar file.
```

## Usage

```
cincan run cincan/jadx <JAR-FILE> -ds <OUTPUTFOLDER.ZIP>
```

```
docker run --rm -v `pwd`:/data cincan/jadx -ds <Output Folder> <JAR/DEX/APK/CLASS/SMALI/ZIP/AAR/ARSC-FILE>

```

## Project homepage

https://github.com/kwart/jd-cmd
