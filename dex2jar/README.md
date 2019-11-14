# Tool to decompile dex files to jar

## Input

```
APK file
```

## Output

```
.jar file created from .apk file

```

## Usage

***Using with cincan-tool***

```
cincan run cincan/dex2jar dex2jar /path/to/apk/file
```


***1. Option A - Clone the repository and build the image***

```
git clone https://gitlab.com/CinCan/dockerfiles
cd dockerfiles/apktools/dex2jar/
docker build . -t cincan/dex2jar
```

***1.Option B - Pull the docker image*** 

```
docker pull cincan/dex2jar
```

***2. Run the docker container***

```
docker run --rm -v `pwd`:/data cincan/dex-tools path/to/your/.apk

```


## Project homepage


[https://github.com/pxb1988/dex2jar]
