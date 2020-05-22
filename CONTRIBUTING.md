# How can I contribute for the tools?

There are many ways to contribute for CinCan tools!

  * By adding [a new tool](#practices-for-adding-a-new-tool)
  * [Upgrading version](#practices-for-upgrading-version-of-the-existing-tool) of the existing tool
  * Optimizing image (reducing size, increasing performance, minimize security permissions)
  * Improving documentation
  * Something else? Please, suggest!


## Practices for adding a new tool

The workflow for adding the new tool usually contains at least:

 * Creation of Dockerfile
   * Adding possible relevant external files required by this specific tool
 * Creation of `meta.json` file
 * Creation of tests
 * Creation of sufficient README file

### Dockerfile

#### Labels

Label for maintainer should be added:

`LABEL MAINTAINER=cincan.io`

#### Tool versions

Each tool should use `ENV` for describing version number of the tool, and use it for installation.

Variable name **must** be `TOOL_VERSION`

- This gives a way for reading version information of the tool from every image/container, just by checking TOOL_VERSION environment variable.
- Dockerfiles can be automatically parsed for documentation, and TOOL_VERSION information can be acquired in this way.
- From Docker Registry API, manifest can be parsed and version information of the tool can be acquired in this way.

To make automatic building attempt for different versions possible in the future, we should use global ARG for defining version variable into actual ENV variable. This helps as well, when defining version variable into last stage in multi-stage builds. (manifest content is based on last stage) This makes defining less error-prone.

For example:

```
ARG tool_version=2.6.1

FROM alpine:latest
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
```

When defining ARG before any image base, value of it can be used in every stage. (However, it should be 'mentioned' in every stage as `ARG tool_version`) Later, each TOOL_VERSION ENV is defined with it. 

There is no other way to use global variables currently.

Tool itself should be latest _stable_ version, and it is installed with previously mentioned TOOL_VERSION environment variable. In this way, we can maintain the actual version of the tool and described version to be identical.

#### Dependency versions and base image version

Usage of specific versions in dependencies leads to extra work, as older dependencies disappear frequently from package managers. Identical analysis environments however can be acquired by using identical build image versions, if that is required.

In general, the version tag for base image should be _latest_ to ensure upgrades of important security updates. However, if someone feels for being able to follow up of all important security updates, usage of precise version is allowed.

Recommended base image type is [**Alpine**](https://hub.docker.com/_/alpine) to minimize the size.

However, sometimes Debian e.g. Buster-slim could offer performance upgrades and better compatibility when compared to Alpine base, since Alpine is not using traditional glibc library.

#### Use checksums

If something is downloaded in build phase from external source(s) as zip etc., use checksums e.g. SHA256 verification to verify that content is, what it is supposed to be.

Example from Ghidra:

```
ENV GHIDRA_SHA256 3d61de711b7ea18bdee3ed94c31429e4946603b3e7d082cca5e949bbd651f051

RUN wget --progress=bar:force -O /tmp/ghidra.zip https://ghidra-sre.org/ghidra_9.1-BETA_DEV_20190923.zip && \
    echo "$GHIDRA_SHA256 /tmp/ghidra.zip" | sha256sum -c -
```

#### Image should run as non-root

Create user named as `appuser` and give required permissions for it to run the tool.

Example for Alpine based image:

```shell
addgroup -S appuser && \
adduser -s /sbin/nologin --disabled-password -G appuser appuser
```

Example for Debian based image:

```shell
groupadd -g 1000 appuser && \
useradd -u 1000 -g appuser -s /sbin/nologin appuser
```

Use the user as early as possible with the line `USER appuser` to ensure clean permissions for the image!

Set working directory for home of this user: `WORKDIR "/home/appuser"` and this is preferably empty.

#### Image size

Image size should be minimized. Whenever there is a benefit from running [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) in a way, that it can reduce size, it should be done.

When installing run-time dependencies, it should be done without storing any cached data. 

If tool contains graphical interface in the same package, can be it be stripped off?

However, image should contain shell (`sh`), otherwise tool cannot be run with `cincan-command`.

### Meta information

When creating Dockerfile for new tool, it is also good to add file **named as 'meta.json'.**

Currently supported attribute is `upstreams` for this JSON file.
This attribute can contain information about the origins of the tools in form of list.

Example below shows, that tool is developed in GitHub, and GitHub is used as source for installation in Dockerfile. By using GitHub releases, upstream tool version information is available and can be also downloaded in this way.

```json
{
  "upstreams": [
    {
      "uri": "https://github.com/radareorg/radare2/",
      "repository": "radareorg",
      "tool": "radare2",
      "provider": "GitHub",
      "method": "release",
      "origin": true,
      "docker_origin": true
    }
  ]
}
```

Multiple sources can be added for different package providers/upstreams.
Example about multiple sources can be seen in [here.](tshark/meta.json)
It is always good to install it directly from very origin instead of other package provider to avoid middlemen.

*This meta information is used to check that Docker image is up to day.* 

For all supported attributes and providers; see more details about upstream checking in [cincan-registry](https://gitlab.com/CinCan/cincan-registry)

### Testing

At least `entrypoint` and `--help` command should be tested for image.
Possible test(s) could be added for real sample, and preferably at least one will be implemented.

This requires sample file, and it should be:

- non-malicious
- free-to-use, preferably created for this purpose

Tests have been implemented by using [_pytest_](https://docs.pytest.org/en/latest/), and the execution is automated with tool named [tox.](https://tox.readthedocs.io/en/latest/)

See reference for [tox.ini](tox.ini)

All tests can be run as:

```
pip install tox
tox
```

Or single test by running:

```
tox <tool-directory-name>
```

Tests are dependant of some the methods of the [cincan tool](https://gitlab.com/CinCan/cincan-command) which is implemented with Python. Currently, at least following methods are available:

- tool_with_file(\_\_file\_\_) - make instance of the tool
- tool.run_get_string([\<POSSIBLE ARGS>]) - for running the tool and getting STDOUT and possible output files

Test wrapper named as `metatool` is used for actually using the `cincan` tool, see source code in [here.](metatool)

#### WIP - resolve unused samples from \_SAMPLES directory:

Following magic can be executed in tools root directory:

```shell
 find _samples -type f | grep -v "$(find . -name "test_*.py" -exec grep  "SAMPLE_FILE.*=" {} \; | tr -d " \"" | awk -F "=" '{print $2}' | sort | uniq -u)" | xargs rm -d
```

This excepts that variable `SAMPLE_FILE` has been used for defining location of the the sample file(s) in test\_\*.py file(s).

In the future, maybe implement testing utility, which should take filename as input, and automatically detects which sample files are unused.

### Licence should be added

If there are no limitations with the licence of the tool, set it as MIT licence. Otherwise, try to be as permissive as possible with tool's own licence.

### Previous leads to following README formatting:

README should describe shortly:

- The purpose of the tool
- Format of input files
- Format of output files
- How to run the tool with 'cincan' wrapper tool
- How to run the tool with docker
- How to run test for this tool, and description of possible sample file
- Credits for the original creator of the tool
  - Project link
  - Maintainer link, twitter handle?
- Licence


## Practices for upgrading version of the existing tool

Upgrading Dockerfile to newer version is straightforward: default value of `ARG tool_version` should be changed to the latest available version for the currently used source in the Dockerfile.


If build process is using checksums (e.g. SHA256), these should be updated as well.

Example beginning of Dockerfile could look something like this:
```
ARG tool_version=2.6.1

FROM alpine:latest
LABEL maintainer=cincan.io

ARG tool_version
ENV TOOL_VERSION=$tool_version
ENV TOOL_SHA256 3d61de711v84a18bdee3ed94c31429e494663l83e7d082cca5e949bbd651f051
```

In ideal case, value change of `tool_version` and `TOOL_SHA256` is enough to upgrade version. However, later versions might bring new dependencies or break something, so that is not always the case.

The source in Dockerfile and the placement of `TOOL_VERSION` variable in there defines the format of the version value.

Once image builds in this way and tests pass (`pytest <tool_name>`), we are ready to merge! If this specific tool is offering version check by CLI, it is also good idea to confirm that it really has been updated.

### Upgrading source in Dockerfile into origin upstream

In case the current source in Dockerfile is not the very origin (holder of the source code), it can be also updated to use it as well; it is recommended to always use this very origin!

This requires also some additional changes. For example, if source in Dockerfile is Debian package, and it is changed to the origin (e.g. GitHub repository), required changes should be added for `meta.json` file. See more about content of that in [here.](#meta-information)