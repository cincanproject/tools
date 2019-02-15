# Generate call graphs from VBA code"

## Input

```
office documents such as .doc, .xls, .bas
```

## Output

```
png: the actual graph image you are looking for
svg: same graph image, just in vector graphics
dot: the dot file which was used to create the graph image
bas: the VBA functions code that was recognized by the script (for debugging)

```


## Build:
```
docker build -t cincan/vba2graph .
```

## Usage

***Office file with macros***
```
docker run --rm -v /samples:/samples -t cincan/vba2graph -f /samples/sample.dotm -o /samples/output/
```

*Olevba generated file or .bas***
```
docker run --rm -v /samples:/samples -t cincan/vba2graph -i /samples/sample.bas -o /samples/output/
```


***Options***  

```  
-h, --help                          :show this help message and exit
-o OUTPUT, --output OUTPUT          :output folder (default: "output")
-c {0,1,2,3}, --colors {0,1,2,3}    :color scheme number [0, 1, 2, 3] (default: 0 - B&W)
```  


## Project homepage

[https://github.com/MalwareCantFly/Vba2Graph](https://github.com/MalwareCantFly/Vba2Graph)
