# CinCan command

The tool `cincan` command provide a frontend
for easier use of the native tools dockerized in the Cincan project.
Currently the frontend is a proof-of-concept with some aspects under construction.

## Installation

As prerequisite you must have installed `Docker` for running the tools,
and `Python 3` and `pip` Python package management program for the command program.
Consult your system documentation how to install them.

The command program is then installed using pip for Python 3:

    % pip3 install CinCan_Command_Program-0.1b0

> ## WARNING
> The image is perhaps not in pip repository,
> FIXME: What to do then!

The python library for command program is now installed, but like to want to insert
the command `cincan` to your path.
For this use the following command to resolve the location of the script `cincan`.

    % python3 -m site --user-base
    /home/username/.local

The actual script should be located as `/bin` under the directory listed above
(with `username` being your user file),
so full path would be `/home/username/.local/bin/`.

Make sure this location is in your Path or create an alias for the command.

NOTE: You may want to install the tool into `virtualenv` to avoid conflicts with
other Python applications you may have. Please consult appropriate documentation.

You can check that all works as follows:

    % cincan list

If all goes well you get a list of the supported tools.
First time running this will take a while as it must fetch information of the tools
and cache it locally.

## Running tools with cincan

### Invoking tools

A tool can be invoked with cincan using 'run' sub-command like this:

    % cincan run <tool> <parameters..>

As you may remember you get the list of supported tools with `cincan list`.
For example the tool `cincan/pywhois`:

    % cincan run cincan/pywhois 127.0.0.1

Many tools give you help information, if you invoke them without arguments, for example:

    % cincan run cincan/tshark

### Input and output files

As the tools are actually ran on docker container, possible input and output files must be
transferred into and out from the container. For this input files are marked with 
`^`-prefix and output files with `^^`-prefix.
For example, if you have file `myfile.pcap`, 
the following command should give you JSON-formatted output from 'tshark':

    % cincan run cincan/tshark -r ^myfile.pcap -Tjson

Or you can invoke `xmldump` with input file `input.xml` and produce output 
to `result.txt` with this command line:

    % cincan run cincan/xmldump -d ^^result.txt text ^input.xml 

An another example is the tool `jsunpack-n` writes the result in directory, which
you can explicitly name with option `-d <dir>`.
The following command line provides an input file for the tool _jsunpack-n_
and also explicitly gives output directory which is then fetched from the
docker container:

    %  cincan run cincan/jsunpack-n ^sample.pdf -d ^^result-dir

## Harmonized tool use with 'do'

Instead of running tools with 'run', you can use the harmonized way to invoking a tool
with sub command 'do', e.g.:

    % cincan do cincan/tshark -r ^myfile.pcap -Tjson
    cincan/tshark: Output to output.tar

This behaves just like 'run' sub-command, but output is put into tar-archive.

FIXME...

The sub command accepts the following arguments

| Argument                | Description                                        |
|-------------------------|----------------------------------------------------|
| --in-file, -f           |  Read a file as input (without ^-prefix)           |
| --in-str, -s            |  Provide input directly as a string                |
| --in, -i                |  Specify the desired input format                  |
| --out, -o               |  Specify the desired output format                 |

You must specify either a file to read or the input directly from command line.
Input or output formats are only required if there are multiple alternatives.

The actual command line for the native tool is created based on the arguments
give for the 'do' sub command.

## Invoking tool without frontend

Sometimes you cannot use the services provided by the 'cincan' frontend.
For example, you wish to provide the files through mounts for their size
rather using the copy approach.

Good luck with that! (seriously, no pun intended)

## Running unit tests

You can run the unit tests of the front and and some test tools like this:

    % PYTHONPATH=`pwd` pipenv run pytest
