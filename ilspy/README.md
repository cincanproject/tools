# ILSpy

A Dotnet assembly decompiler and portable PDB generator. 

[Reference to PDB.](https://github.com/dotnet/core/blob/master/Documentation/diagnostics/portable_pdb.md)

## Supported tags and respective `Dockerfile` links

* `latest` 
([*ilspy/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/dotnetdecompile))


## Input

```
.NET Assembly
```

## Output

```
Decompiled source code in C# or PDB
```

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

`$ docker run -v /samples:/samples cincan/ilspy /samples/ilspysample.exe`


## Project homepage

https://github.com/icsharpcode/ILSpy

### Nuget repository for cmd-only:

https://www.nuget.org/packages/ilspycmd/

## Licence

Distributed under same terms (MIT) than ILSpy itself.
