# box-ps - A Powershell sandboxing utility used to deobfuscate PowerShell scripts

A Powershell sandboxing utility by [Connor Shride](https://github.com/ConnorShride) used to deobfuscate PowerShell scripts

## Input

```
ps1, psm1
```

## Output

```
ps1, json
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*box-ps/Dockerfile*](https://gitlab.com/CinCan/tools/blob/master/stable/box-ps/Dockerfile))

## Usage

While using the [`cincan`](https://gitlab.com/cincan/cincan-command) tool,
analyze a PowerShell script `example.ps1` to an directory `output` with a
timeout of 10 seconds, without network connectivity

```
cincan run --network=none box-ps -InFile example.ps1 -OutDir output -Timeout 10
```

While using `docker` directly, place `example.ps1` in absolute directory <SAMPLES> and use a volume mount:

```
docker run --network=none --rm -v <SAMPLES>:/samples cincan/box-ps -InFile /samples/example.ps1 -OutDir /samples/output -Timeout 10
```
