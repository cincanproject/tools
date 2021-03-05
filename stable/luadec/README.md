# luadec: Lua decompiler

LuaDec is a Lua decompiler for lua 5.1 bytecode

## Input

```
.luac .lua
```

## Output

```
lua source code
```

## Supported tags and respective `Dockerfile` links
* `latest` ([*luadec/Dockerfile*](Dockerfile))

## Usage

Using the `cincan` command to decompile lua bytecode file:

```
cincan run cincan/luadec compiled.luac
```

Using the docker command to achieve the same:

```
docker run --rm -v `pwd`:/data cincan/luadec compiled.lua
```

## Changing entrypoint

Luadec has two additional binaries, `luaopswap` and `luareplace`. You can access them by changing entrypoint, for example
```
cincan run --entrypoint /usr/local/bin/luaopswap cincan/luadec <input>
```

## Project homepage

[Project GitHub viruscamp/luadec](https://github.com/viruscamp/luadec)
