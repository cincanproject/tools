## CinCan command

The tool `cincan` command provide a frontend
for easier use of the native tools dockerized in the Cincan project.
Currently the frontend is a proof-of-concept with some aspects under construction.

> ## WARNING
> Currently only a few or none of the repositories in DockerHub contain the required
> metadata for any of the following to work!

### Installation

As prerequisite you must have installed `Docker` for running the tools,
and `Python 3` and `pip` Python package management program for the command program.
Consult your system documentation how to install them.

The command program is then installed using pip for Python 3:

    % pip3 install CinCan_Command_Program-0.1b0

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

### Using it now

### Tool inputs and outputs

The supported tools have the allowed input and output data types listed, 
so that you can easily figure out which tools are suitable for your data.
The tools and input and output data types are listed by the sub command 'list'
like this:

    % cincan list -i -o

The output is made from columns of tool name, input types, output types. 
The list of supported arguments are:

| Argument                | Description                                        |
|-------------------------|----------------------------------------------------|
| --in, -i                |  List possible input formats                       |
| --out, -o               |  List possible output formats                      |
| --tags, -t              |  List all docker tags (tool versions)              |

Note only a subset of all tools have the required metadata to give hints.
If the data is not available, you get the following output:

    % cincan hint <tool-without-metadata>
    ...
    No command hints

### Command line hints

For some tools you can get command line hints by sub command 'hint':

    % cincan hint <tool>

for example

    % cincan hint cincan/tshark
    run cincan/tshark -r ^<file> -Tjson
    run cincan/tshark -r ^<file> -Tpdml

You can then invoke the actual too using sub command 'run', 
For example, if you have file `myfile.pcap`, 
the following command should give you JSON-formatted output from 'tshark':

    % cincan run cincan/tshark -r ^myfile.pcap -Tjson

Please note that the __`^`-character is a required prefix__ for a file given in command line, 
as it marks which parameters are actually files. This information is required
to upload the required files into Docker container before running the actual tool.

You can still access the native help of a tool with tool-specific way, 
usually providing parameter `-h` or `--help`. For example:

    % cincan run cincan/tshark --help

Finally note that you are free to invoke the native tool in any supported way
irrelevant of which hints, if any, are available. Just remember to prefix
all filenames with `^` so that they get uploaded to docker image.

#### Access output files

Some tools put their output into files. Normally, these files remain only in the
docker container and are destroyed with the container.
However, you can fetch output files by marking the files in command line with
prefix `^^`-prefix.

For example the tool _jsunpack-n_ writes the result in directory, which
you can explicitly name with option `-d <dir>`.
The following command line provides an input file for the tool _jsunpack-n_
and also explicitly gives output directory which is then fetched from the
docker container:

    %  cincan run cincan/jsunpack-n ^sample.pdf -d ^^result-dir

### Harmonized tool input

Instead of looking at tool hints, you can use the harmonized way to invoking a tool
with sub command 'do', e.g.:

    % cincan do --read-file myfile.pcap --out application/json cincan/tshark

Note that we did not use the `^`-prefix. 

The sub command accepts the following arguments

| Argument                | Description                                        |
|-------------------------|----------------------------------------------------|
| --read-file, -r         |  Read a file as input (without ^-prefix)           |
| --in-str, -s            |  Provide input directly as a string                |
| --in, -i                |  Specify the desired input format                  |
| --out, -o               |  Specify the desired output format                 |

You must specify either a file to read or the input directly from command line.
Input or output formats are only required if there are multiple alternatives.

The actual command line for the native tool is created based on the arguments
give for the 'do' sub command.

### Invoking tool without frontend

Sometimes you cannot use the services provided by the 'cincan' frontend.
For example, you wish to provide the files through mounts for their size
rather using the copy approach.

Good luck with that! (seriously, no pun intended)

### Running unit tests

You can run the unit tests of the front and and some test tools like this:

    % PYTHONPATH=`pwd` pipenv run pytest
