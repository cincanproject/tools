# Analytical decompiler for Java

JetBrains developed Java decompiler for IntelliJ IDEA

## Input

```
.jar, .class, .zip
```

## Output

```
.jar with decompiled `.java` files
```

## Usage

```
cincan run cincan/fernflower compiled.jar samples/decompiled
```

```
docker run --rm -v `pwd`/samples:/samples cincan/fernflower compiled.jar samples/decompiled
```

For advanced usage, see project GitHub repository

## Project homepage
[JetBrains intellij-community GitHub repository](https://github.com/JetBrains/intellij-community/tree/master/plugins/java-decompiler/engine)


## License

[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)
