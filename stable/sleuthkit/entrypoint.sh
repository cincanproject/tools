#!/bin/sh

case $1 in help)
    printf "Available tools:\n"
    for tool in /usr/local/bin/*; do
        tool=$(basename $tool)
        printf "  ${tool}\n";
    done;
    exit 0
esac

exec "$@"

