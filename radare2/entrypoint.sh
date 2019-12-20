#!/bin/env/sh

# Wrapper for oletools for Dockerimage
# See project homepage: https://github.com/decalage2/oletools

# Exit script if command fails
set -o errexit
# Exit if script attempts to use undeclared variables
set -o nounset

help() {
    printf "\n  This is shell script wrapper for radare2\n"
    printf "  Following tools are available. See '--help' for each tool if needed.\n\n"
    printf "  %s\n\n" "USAGE: <toolname> ARGS"

    for tool in "$R2_HOME"/*; do
        tool="$(basename "$tool")"
        printf "    %s\n" "${tool}"
    done
    echo ""
    exit 0
}

case ${1-} in "" | "-h" | "--help")
    help
    ;;
"script" | "--script")
    for script in "$R2_SCRIPTS"/*; do
        tool="$(basename "$script")"
        if [ "$script" = "${1}" ]; then
            sh "$@"
            exit 0
        fi
    done
    ;;
-? | -*)
    printf '\n  WARNING: Unknown option (ignored): %s\n' "$1" >&2
    help
    ;;
*)
    for tool in "$R2_HOME"/*; do
        tool="$(basename "$tool")"
        if [ "$tool" = "${1}" ]; then
            exec "$@"
            exit 0
        fi
    done
    # Print notification about invalid toolname with red ANSI code
    echo -e "\n  \e[31mInvalid toolname '$1'.\e[0m\n"
    help
    ;;
esac
