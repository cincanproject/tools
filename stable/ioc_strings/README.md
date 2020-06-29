# Extracts urls, hashes, emails, ips, domains and base64 (other) from a file.

## Input

```
File/Directory
```

## Output

```
json
```


## Supported tags and respective `Dockerfile` links

* `latest` 
([*ioc_strings/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/ioc_strings/Dockerfile))


## Usage

Get usage using the _cincan_ CLI:  

```bash
cincan run cincan/ioc_strings --help
```

Get IoCs from a file:  

```bash
cincan run cincan/ioc_strings <SAMPLE>
```

Get IPs Using the _docker_ command:  

```bash
docker run -v <SAMPLES>:/samples cincan/ioc_strings --filter IP <SAMPLE>
```


## Project homepage

https://gitlab.com/CinCan/ioc_strings


## License

[MIT](https://choosealicense.com/licenses/mit/)
