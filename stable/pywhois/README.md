# Pywhois - retrieve information from IP addresses

Retrieve information of IP addresses using Python 'whois' module.

In the  [CinCan project](https://cincan.io) project we have dockerized many analysis tools,
one of them being Python 'whois'.

## Input

```
IP / list of IPs
```

## Output

```
report in JSON
```

## Usage

### Using cincan command

The [cincan](https://gitlab.com/cincan/cincan-command) command makes it almost as easy
to use dockerized tools than tools installed natively (without need to install them individually).
You can get cincan command from PyPI, e.g. (check your Python documentation for details):

    $ sudo pip3 install cincan-command

After that it is straightforward to invoke the dockerized 'pywhois' for a IP(s) using the
cincan command:

    $ cincan run cincan/pywhois <IP>

Or scan through a list of IPs specified in a file:

    $ cincan run cincan/pywhois -f <FILE>

### Using docker

You can use the dockerized 'pywhois' tool also directly with docker cli:

    $ docker run --rm cincan/pywhois <IP>
