# Manalyze

# "A static analyzer for PE executables"

## Input

```
PE files
```

## Output

```
Manalyze report
```

## Supported tags and respective `Dockerfile` links

* `latest` 
([*manalyze/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/manalyze))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/manalyze
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/manalyze
docker pull cincan/manalyze
```

***3. Run the docker container***

Analyse a sample in directory "/samples":

`$ docker run -v /samples:/samples -ti cincan/manalyze /samples/pe.exe`  

Analyze all files in the folder:  

`$ docker run -v /samples:/samples -ti cincan/manalyze -r /samples`  


## Project homepage

https://github.com/JusticeRage/Manalyze
