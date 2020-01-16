# John the Ripper for extracting hash from PDF files

## Input

```
Encrypted PDF
```

## Output

```
Hash
```

## Supported tags and respective `Dockerfile` links
* `latest`  
([*pdf2john/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/pdf2john/Dockerfile))

## Usage

1. Clone the repository

```
git clone https://gitlab.com/CinCan/tools
cd dockerfiles/pdf2john/
```

2. Build OR pull the docker image

```
docker build . -t cincan/pdf2john
docker pull cincan/pdf2john
```

3. Run the docker container

```
docker run -v /samples:/samples cincan/pdf2john /samples/encrypted.pdf
```

## Project homepage

https://github.com/magnumripper/JohnTheRipper
