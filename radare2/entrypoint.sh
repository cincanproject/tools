#!/bin/env/sh

# Wrapper for radare2 for Dockerimage
# See project homepage: https://github.com/radareorg/radare2

# Exit script if command fails
set -o errexit
# Exit if script attempts to use undeclared variables
set -o nounset

help() {
    printf "\n  This is shell script wrapper for radare2.\n"
    printf "  There is one available subcommand: 'script' to specify executable script instead of tool shown below.\n"
    printf "  Following tools are available. See '-h' for each tool if needed.\n\n"
    printf "  %s\n\n" "USAGE: <toolname> ARGS"

    for tool in "$R2_HOME"/*; do
        tool="$(basename "$tool")"
        printf "    %s\n" "${tool}"
    done
    echo ""
    exit 0
}

help_script() {
    printf "  'script' command needs script as argument.\n\n"
    printf "  %s\n\n" "USAGE: script <script_name> ARGS"

    for script in "$R2_SCRIPTS"/*; do
        script="$(basename "$script")"
        printf "    %s\n" "${script}"
    done
    echo ""
    exit 0

}

case ${1-} in "" | "-h" | "--help")
    help
    ;;
"script" | "--script")
    for script in "$R2_SCRIPTS"/*; do
        script="$(basename "$script")"
        if [ "$script" = "${2-}" ]; then
            shift 2
            sh "$R2_SCRIPTS/$script" "$@"
            exit 0
        fi
    done

    echo -e "\n  \e[31mInvalid script name or no script provided.\e[0m\n"
    help_script
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
