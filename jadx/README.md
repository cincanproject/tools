# "Dex to Java decompiler"

## Input

```
(.apk, .dex, .jar, .class, .smali, .zip, .aar, .arsc)
```

## Output

```
Folder with java files
```
## Usage

```
docker run --rm -v `pwd`:/data cincan/jadx -d <Output Folder> <JAR/DEX/APK/CLASS/SMALI/ZIP/AAR/ARSC-FILE>

options:
  -d, --output-dir                    - output directory
  -ds, --output-dir-src               - output directory for sources
  -dr, --output-dir-res               - output directory for resources
  -r, --no-res                        - do not decode resources
  -s, --no-src                        - do not decompile source code
  --single-class                      - decompile a single class
  --output-format                     - can be 'java' or 'json', default: java
  -e, --export-gradle                 - save as android gradle project
  -j, --threads-count                 - processing threads count, default: 4
  --show-bad-code                     - show inconsistent code (incorrectly decompiled)
  --no-imports                        - disable use of imports, always write entire package name
  --no-debug-info                     - disable debug info
  --no-inline-anonymous               - disable anonymous classes inline
  --no-replace-consts                 - don't replace constant value with matching constant field
  --escape-unicode                    - escape non latin characters in strings (with \u)
  --respect-bytecode-access-modifiers - don't change original access modifiers
  --deobf                             - activate deobfuscation
  --deobf-min                         - min length of name, renamed if shorter, default: 3
  --deobf-max                         - max length of name, renamed if longer, default: 64
  --deobf-rewrite-cfg                 - force to save deobfuscation map
  --deobf-use-sourcename              - use source file name as class name alias
  --rename-flags                      - what to rename, comma-separated, 'case' for system case sensitivity, 'valid' for java identifiers, 'printable' characters, 'none' or 'all' (default)
  --fs-case-sensitive                 - treat filesystem as case sensitive, false by default
  --cfg                               - save methods control flow graph to dot file
  --raw-cfg                           - save methods control flow graph (use raw instructions)
  -f, --fallback                      - make simple dump (using goto instead of 'if', 'for', etc)
  -v, --verbose                       - verbose output (set --log-level to DEBUG)
  -q, --quiet                         - turn off output (set --log-level to QUIET)
  --log-level                         - set log level, values: QUIET, PROGRESS, ERROR, WARN, INFO, DEBUG, default: PROGRESS
  --version                           - print jadx version
  -h, --help                          - print this help

Example:
 jadx -d out classes.dex
 jadx --rename-flags "none" classes.dex
 jadx --rename-flags "valid,printable" classes.dex
 jadx --log-level error app.apk

```

## Project homepage

https://github.com/kwart/jd-cmd
