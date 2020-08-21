# A tool for reverse engineering 3rd party, closed, binary Android apps.

## Input

```
.apk, .jar

```

## Output

```
Folder with decompiled application files
```

## Usage
```
cincan run cincan/apktool d apk_file.apk -o output_file
```

```
docker run --rm -v `pwd`:/data cincan/apktool:dev d apk_file.apk

```

## Project homepage 

[https://ibotpeaches.github.io/Apktool/]