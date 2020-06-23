# Flawfinder - Finds possible security weaknesses in C/C++ source code

"flawfinder" by David A. Wheeler.

Flawfinder is a simple program that scans C/C++ source code and reports potential security flaws. It supports the Common Weakness Enumeration (CWE) and is officially CWE-Compatible.

### Input  

```
C/C++ code
```

### Output

```
Flawfinder report
```

## Usage

By using `cincan-command` tool:

`cincan run cincan/flawfinder sample.c`

Or by using Docker:

`docker run -v /samples:/samples cincan/flawfinder /samples/sample.c`

## Project homepage

https://github.com/david-a-wheeler/flawfinder

## Licence

 GNU GPL License version 2 or later (GPL-2.0+).