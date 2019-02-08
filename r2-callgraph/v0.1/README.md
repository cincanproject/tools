# Modificated Radare2 image that analyzes passed input binaries and generates Graphviz dot files and PNG images as a result

## Input

```
ELF and/or PE binaries
```

## Output

```
DOT (graph description language), PNG
```

## Supported tags and respective `Dockerfile` links

* `0.0` ([*r2-callgraph/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/r2-callgraph/v0.0/Dockerfile))
* `0.1` ([*r2-callgraph/Dockerfile*](https://gitlab.com/CinCan/dockerfiles/blob/master/r2-callgraph/v0.1/Dockerfile))

## Usage

Following steps are required to perform to get correct results.


***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/dockerfiles
cd dockerfiles/r2-callgraph/v0.1/
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/r2-callgraph:0.1
docker pull cincan/r2-callgraph:0.1
```
***3. Create directory and add samples to it***

```
mkdir ./samples
cp /path/to/samples/* ./samples
```

***4. Run the docker container***
```
docker run --rm -it -v $(pwd):/r2 cincan/r2-callgraph:0.1
```

***5. List the results***
ls ./results/dot/* ./results/images/*



## Project homepage

https://github.com/radare/radare2
