# Manalyze - a static analyzer for PE executables

Manalyze was built for providing better analysis information than anti virus products - to tell more about why the file could be malicious.

Based on project home page, it could do at least:

* Identifies a PE's compiler
* Detects packed executables
* Applies ClamAV signatures
* Searches for suspicious strings
* Looks for malicious import combinations (i.e. WriteProcessMemory + CreateRemoteThread)
* Detects cryptographic constants (just like IDA's findcrypt plugin)
* Can submit hashes to VirusTotal
* Verifies authenticode signatures (on Windows only)


## Input

```
PE files
```

## Output

```
Manalyze report
```

## Usage

With CinCan command to get basic analysis of file:

```
cincan run cincan/manalyze --pe sample_pe.exe
```

```
cincan run cincan/manalyze --help
```


With docker: 

```
docker run -v /samples:/samples cincan/manalyze /samples/sample.c`
```

```
docker run --rm cincan/manalyze --help
``` 
## Project homepage

https://github.com/JusticeRage/Manalyze


## Licence

GPLv3