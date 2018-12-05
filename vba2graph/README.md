# Vba2Graph

## Build:
```
docker build -t cincan/vba2graph .
```

## Usage for Office file with macros:
```
docker run --rm -v /samples:/samples -t cincan/vba2graph -f /samples/sample.dotm -o /samples/output/
```

## Usage for olevba generated file or .bas:
```
docker run --rm -v /samples:/samples -t cincan/vba2graph -i /samples/sample.bas -o /samples/output/
```
