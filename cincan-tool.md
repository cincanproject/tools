## Tool 'cincan'

Tool frontend 'cincan' provide a frontend for easier use of the tools dockerized in the 
Cincan project.
Currently the frontend is a proof-of-concept with some aspects under construction.
Especially it is undecided how the this should be deployed to the users. 
Part of the frontend should also be itself containerized?

The python file dockertools.py (and some other files) provide the current implementation.

> ## WARNING
> Currently only a few or none of the repositories in DockerHub contain the required
> metadata for any of the following to work!


### Using it now

The steps required currently to set 'cincan' for Linux:

 1. Install `docker`, `python`, and `pipenv`
 2. Clone the repository, and start new virtualenv
 
        % git clone git@gitlab.com:CinCan/tools.git
        % cd tools
        % pipenv shell
         
 3. Install required python modules 

        % pipenv install docker
        % pipenv install pytest  (only required for unit tests)
         
 4. Create alias 'cincan'
 
        % alias cincan="python3 dockertools.py"

You can check that all works as follows:

    % cincan list

If all goes well you get a list of the supported tools.

### Tool inputs and outputs

The supported tools have the allowed input and output data types listed, 
so that you can easily figure out which tools are suitable for your data.
The tools and input and output data types are listed by the subcommand 'list'
like this:

    % cincan list

The output is made from columns of: tool name, input types, output types

The list is compiled from metadata LABELs inside dokertized tools, 
as seen in this clip from `Dockerfile` for the tool 'tshark':

    LABEL io.cincan.input="application/pcap"
    LABEL io.cincan.output="application/json,text/xml"

### Command line hints

For some tools you can get command line hints by subcommand 'hint':

    % cincan hint <tool>

for example

    % cincan hint cincan/tshark
    run cincan/tshark -r ^<file> -Tjson
    run cincan/tshark -r ^<file> -Tpdml

You can then invoke the actual too using sub command 'run', 
For example, if you have file `myfile.pcap`, 
the following command should give you JSON-formatted output from `tshark`:

    % cincan run cincan/tshark -r ^myfile.pcap -Tjson

Please note that the `^`-character is a __required prefix__ for a file given in command line, 
as it marks which parameters are actually files. This information is required
to upload the required files into Docker container before running the actual tool.

You can still access the native help of a tool with tool-specific way, 
usually providing parameter `-h` or `--help`. For example:

    % cincan run cincan/tshark --help
    
### Harmonized tool input

Instead of looking at tool hints, you can use the harmonized way to invoking a tool
with sub command 'do', e.g.:

    % cincan do --read-file myfile.pcap --out application/json cincan/tshark

Note that we did not use the `^`-prefix. 

The sub command accepts the following arguments

| Argument                | Description                                        |
|-------------------------|----------------------------------------------------|
| --read-file, -r         |  Read a file as input (without ^-prefix)           |
| --in-str                |  Provide input directly as a string                |
| --in                    |  Specify the desired input format                  |
| --out                   |  Specify the desired output format                 |

You must specify either a file to read or the input directly from command line.
Input or output must be specified if there are multiple alternatives.
The actual command line for the native tool is created based on the arguments
give for the 'do' sub command.

