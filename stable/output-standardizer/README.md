# Generate md report from Cincan's Concourse pipelines, or convert single tool output to JSON.  

Generate a Markdown report from CinCan project's result files of a specific Concourse pipeline,  

Or standardize single tool output data from plain text into to JSON format.  

## Input

```
cincan/binwalk, cincan/pdf2john, cincan/pdfxray_lite and cincan/strings outputs
```

## Output

```
json / markdown
```

## Supported tags and respective `Dockerfile` links

* `latest` ([*output-standardizer/Dockerfile*](https://gitlab.com/CinCan/tools/tree/master/output-standardizer))


## Usage


Standardize pdfxray_lite report in folder "samples" using cincan-command (note that --quiet must be set):

`$ cincan run cincan/output-standardizer json --quiet --input /samples/pdfxray_lite_report.html --output /samples/output.json -t pdfxray_lite`  

Standardize binwalk output using Docker command:  

`$ docker run --rm -v /samples:/samples cincan/output-standardizer json --quiet -i output/binwalk_output.txt -o output/binwalk_output_standardized.json -t binwalk
`  

Produce a markdown report from the document-pipeline's results files:  

`$ cincan run cincan/output-standardizer markdown document-pipeline /path/to/results/ -o my_report_filename`


## Project homepage

[https://gitlab.com/CinCan/tools-output-standardization](https://gitlab.com/CinCan/tools-output-standardization)


## License

[MIT](https://choosealicense.com/licenses/mit/)
