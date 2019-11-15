# ILSpy (console only) - version 5.0.2

A Dotnet assembly decompiler and portable PDB generator. 

[Reference to PDB.](https://github.com/dotnet/core/blob/master/Documentation/diagnostics/portable_pdb.md)

## Supported tags and respective `Dockerfile` links

* `latest` 
([*ilspy/Dockerfile*](Dockerfile))


## Input

```
.NET Assembly
```

## Output

```
Decompiled source code in C#, PDB or Visual Studio Project
```

## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/ilspy
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/ilspy
docker pull cincan/ilspy
```

***3. Run the docker container***

Analyse a sample in directory "/samples":  

`$ docker run -v /samples:/samples cincan/ilspy /samples/ilspy_sample.exe`


## Testing

Few tests are included for testing the functionality of container. These contains at least:

  * Decompile without options
  * Decompile only PDB file

### Sample file

Sample file was created for CriM-2019 workshop (Compiled binary C# .NET Assembly). It contains simple dropper for malicous binary from remote URL.

## Project homepage

https://github.com/icsharpcode/ILSpy

### NuGet repository of console-only:

https://www.nuget.org/packages/ilspycmd/

## Licence

Distributed under same terms (MIT) than ILSpy itself.
