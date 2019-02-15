# Generate call graphs from VBA code"

## Input

```
PDF, URL, PCAP, JavaSCript, SWF
```

## Output

```
jsunpack-n report
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
