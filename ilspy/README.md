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

### Installation

***Method 1. Clone the repository and build by yourself***

```
git clone https://gitlab.com/CinCan/tools
cd tools/ilspy
docker build . -t cincan/ilspy
```

***Method 2. Pull the docker image*** 

```
docker pull cincan/ilspy
```

***Method 3. use ['cincan'](https://gitlab.com/CinCan/cincan-command) tool*** 

Follow 'cincan' tool installation steps. If this tool is used, no need to install 'ILSpy' separately.

### Running

***Method 1. Run the docker container***

Analyse a sample in directory "/samples":  

`$ docker run -v /samples:/samples cincan/ilspy /samples/ilspy_sample.exe`

Or get possible arguments for the program:  

`$ docker run -v /samples:/samples cincan/ilspy --help`

***Method 2. Run with 'cincan' tool:***

Analyse a provided example sample from this directory:

`$ cincan run cincan/ilspy samples/ilspy_sample.exe`

Get help for specifically this tool:

`$ cincan run cincan/ilspy --help `

## Testing

Few tests are included for testing the functionality of container. These contains at least:

  * Decompile without options
  * Decompile only PDB file
  * Decompile as Visual Studio Project

### Sample file

Sample file was created for CriM-2019 workshop (Compiled binary C# .NET Assembly). It contains simple dropper for malicous binary from remote URL.

## Project homepage

https://github.com/icsharpcode/ILSpy

### NuGet repository of console-only:

https://www.nuget.org/packages/ilspycmd/

## Licence

Distributed under same terms (MIT Licence) than ILSpy itself.
