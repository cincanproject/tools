# Pywhois

## Retrieve information of IP addresses

## Input

```
IP / list of IPs
```

## Output

```
report in JSON
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*pywhois/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/pywhois))


## Usage

***1. Clone the repository***

```
git clone https://gitlab.com/CinCan/tools
cd tools/pywhois
```

***2. Build OR pull the docker image*** 

```
docker build . -t cincan/pywhois
docker pull cincan/pywhois
```

***3. Run the docker container***

Get information of an IP:  

`$ docker run --rm cincan/pywhois <IP>`  


Scan through a list of IPs:

`$ docker run --rm cincan/pywhois f <FILE>`  

