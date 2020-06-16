# PDFID

Scan PDFs for certain keywords, Javascript, auto-open functions etc.

In the  [CinCan project](https://cincan.io) project we have dockerized many analysis tools,
one of them being [pdfid from Didier Stevens](https://blog.didierstevens.com/programs/pdf-tools/#pdfid)


## Input

```
PDF
```

## Output

```
PDFiD report
```

## Usage

### Using the cincan tool

The [cincan](https://gitlab.com/cincan/cincan-command) command makes it almost as easy
to use dockerized tools than tools installed natively (without need to install them individually).
You can get cincan command from PyPI, e.g. (check your Python documentation for details):

    $ sudo pip3 install cincan-command

After that it is straightforward to invoke the dockerized 'pdfid' for a pdf-file using the
cincan command:

    $ cincan run cincan/pdfid <pdf-file>

For example, using a sample file from the `_samples/` directory:

    $ cincan run cincan/pdfid _samples/pdf/text_txt.pdf
    cincan/pdfid: <= _samples/pdf/text_txt.pdf
    PDFiD 0.2.5 _samples/pdf/text_txt.pdf
     PDF Header: %PDF-1.4
     obj                   13
    ...

There are several options to configure pdfid, for quick help run the command without arguments:

    $ cincan run cincan/pdfid <pdf-file>


For example, use the following to run with triage-plugin:

    $ cincan run cincan/pdfid _samples/pdf/text_txt.pdf -p plugin_triage
    ...
    Triage plugin score:        0.00
    Triage plugin instructions: Sample is likely not malicious, unless you suspect this is used in a targeted/sophisticated attack

For details of the tool, go to the home page of the tool:
[https://blog.didierstevens.com/programs/pdf-tools/#pdfid](https://blog.didierstevens.com/programs/pdf-tools/#pdfid)

### Using docker

You can use the dockerized 'pdfid' tool also directly with docker cli, but you
need to use volument to get the analyzed PDF document, e.g.:

    $docker run -v `pwd`/_samples:/samples cincan/pdfid /samples/pdf/text_txt.pdf

## Tool homepage

[https://blog.didierstevens.com/programs/pdf-tools/#pdfid](https://blog.didierstevens.com/programs/pdf-tools/#pdfid)
