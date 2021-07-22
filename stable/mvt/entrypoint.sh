#!/bin/env/bash

# Wrapper for MVT tool to combine mvt-ios and mvt-android commands
# See project homepage https://github.com/mvt-project/mvt

# Exit script if command fails
set -o errexit
# Exit if script attempts to use undeclared variables
set -o nounset

help() {
    printf "\n  This is unofficial shell script wrapper for Mobile Verification Toolkit to be used in Docker container.\n"
    printf "\n  Project home: https://github.com/mvt-project/mvt\n"
    printf "  Following subcommands are available. See '--help' for each command if needed.\n\n"
    printf "  %s\n\n" "USAGE: <toolname> ARGS"
    printf "    %s\n" "mvt-ios"
    printf "    %s\n" "mvt-android"
    echo ""
    exit 0
}

case ${1-} in "" | "-h" | "--help")
    help
    ;;
"mvt-ios" | "--mvt-ios")
    shift 1
    mvt-ios "$@"
    exit 0
    ;;
"mvt-android" | "--mvt-android")
    shift 1
    # echo "Android forensics requires ADB. Listing available devices..."
    # echo "You must accept connection from your phone in 5 seconds."
    mvt-android "$@"
    exit 0
    ;;
-? | -*)
    printf '\n  WARNING: Unknown option (ignored): %s\n' "$1" >&2
    help
    ;;
*)
    printf '\n  WARNING: Unknown option (ignored): %s\n' "$1" >&2
    help
    ;;
esac