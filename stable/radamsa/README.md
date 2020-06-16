# "Radamsa is a test case generator for robustness testing, a.k.a. a fuzzer."

Radamsa is the great open source command-line fuzzer for all purposes created by Aki Helin.
Aki describes Radamsa like this:

> Radamsa is a test case generator for robustness testing, a.k.a. a fuzzer. It is typically used to test how well a program can withstand malformed and potentially malicious inputs. It works by reading sample files of valid data and generating interestringly different outputs from them. The main selling points of radamsa are that it has already found a slew of bugs in programs that actually matter, it is easily scriptable and, easy to get up and running.

Radamsa was originally created in the [OUSPG](https://www.oulu.fi/bisg/ouspg) research group.

## Input

```
Any data
```

## Output

```
Any data++
```

## Usage

### Get help

Get command line help of the tool this way, using the
[`cincan`](https://gitlab.com/cincan/cincan-command) tool:
```
cincan run cincan/radamsa --help
```

or using `docker` directly

```
docker run --rm cincan/radamsa --help
```

### Fuzzing a file

Read file 'hello.txt' and produce 10 fuzzed versions of it into directory `fuzzed/`,
with the help of `cincan` tool:

```
cincan run --mkdir "fuzzed" cincan/radamsa -n 10 -o "fuzzed/%n" hello.txt
```

Radamsa argument `-n 10` requests 10 fuzzed files.
Cincan tool argument `--mkdir fuzzed` creates the result directory and avoids uploading
possible existing fuzzed files into the container.

Alternatively you can use the `docker run` command and mounting directories to container
(you must create directory `fuzzed` beforehand):

``` 
docker run --rm -v $(pwd):/files cincan/radamsa -n 10 -o "/files/fuzzed/%n" /files/hello.txt
```

## Project homepage

https://gitlab.com/akihe/radamsa

