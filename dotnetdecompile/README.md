# DotNetDecompile

A Dotnet decompiler  

## Supported tags and respective `Dockerfile` links

* `latest` 
([*dotnetdecompile/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/dotnetdecompile))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/dotnetdecompile
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/dotnetdecompile
docker pull cincan/dotnetdecompile
```

***3. Run the docker container***

Analyse a sample in directory "/samples":  

`$ docker run -v /samples:/samples cincan/dotnetdecompile /samples/dotnetsample.exe`


## Project homepage

https://www.nuget.org/packages/ilspycmd/
