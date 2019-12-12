#!/usr/bin/env bash
# POSIX

# MIT License

# Copyright (c) 2019 Authors of CinCan project

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Use for debuggin
# set -o xtrace

# Exit script if command fails
set -o errexit
# Exit if script attempts to use undeclared variables
set -o nounset

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file})"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app

help() {
    echo ""
    echo -e "  \e[93mDecompiler."
    echo -e "  "
    echo -e "  Some of the options have been disabled due to being unusable with container.\e[0m"
    echo ""
    echo "  USAGE: <command> [<optional args>] INPUT_FILE"
    echo ""
    echo "      [-preScript <ScriptName>] - name of the pre-script. Expected to be located on Ghidra's default location."
    echo "      [-postScript <ScriptName>] - name of the post-script. Expected to be located on Ghidra's default location."
    echo "      [-scriptPath \"<path1>[;<path2>...]\"] - Path(s) of the possible external scripts. Seperate multiple paths with semicolon."
    #${__headless_path} --help
    exit 0
}

subcommand_help() {

    echo ""
    echo ""
    echo -e "  \e[93mThis is shell script wrapper around 'Ghidra Headless Analyzer'."
    echo -e "  It attemps to provide some default options for easier analysis from Docker container."
    echo -e "  Some of the options have been disabled due to being unusable with container.\e[0m"
    echo ""
    echo -e "  Additionally there is set of utilities for helping for defining possible arguments."

    echo "  USAGE: <command> [<optional args>]"
    echo ""
    echo "  list"
    echo "  decompile"
    echo ""

    exit 0
}

list_processors() {
    echo ""
    echo "  Supported processor architectures: "
    echo ""
    find "${GHIDRA_HOME}/Ghidra/Processors" -mindepth 1 -maxdepth 1 -printf "\t%-15f\n" | sort
    echo ""
    exit 0
}

list_language_ids() {

    echo ""
    echo "  Supported languageID:s of selected processor:"
    echo ""
    find "${GHIDRA_HOME}/Ghidra/Processors/${PROCESSOR}/data/languages"  -mindepth 1 -maxdepth 1 -name "*.ldefs" -printf "\t%-15f\n" -exec cat {}  \; #| grep "id"
    exit 0
}

if [ -z "${GHIDRA_HOME-}" ]; then
    GHIDRA_HOME="/opt/ghidra/ghidra_9.1_PUBLIC"
fi

__headless_path="${GHIDRA_HOME}/support/analyzeHeadless"
__projects_path="${GHIDRA_HOME}/projects"

arg1="${1:-}"

#echo "$1"

#help
if [ -z "${1+x}" ]; then
    echo ""
    echo "  No arguments given."
    echo "  Please, give at least a file or directory to be analyzed."
    subcommand_help
fi

# Check for subcommand, whether it is list or decompile.

subcommand="${1:-}"
# echo -n $subcommand
case $subcommand in
"" | "-h" | "--help")
    subcommand_help
    ;;
list)
    if [ "${2-}" = "processors" ]; then
        if [ "${3-}" ]; then
            PROCESSOR="${3}"
            list_language_ids
        else
            list_processors
        fi
        shift
    else
        echo ""
        echo "  List requires an argument."
        subcommand_help
    fi
    ;;
*)
    shift
    ${subcommand} $@
    if [ $? = 127 ]; then
        echo "Error: '$subcommand' is not a known subcommand." >&2
        echo "       Run '$ProgName --help' for a list of known subcommands." >&2
        exit 1
    fi
    ;;
esac

TARGET_FILES=""

while :; do
    # echo "${1}"
    case "${1+x}" in
    # -import)
    #     IMPORT_PATH="${1}"
    #     if [ "$2" ]; then
    #         RECURSIVE="-recursive"
    #         shift
    #     fi;;
    -preScript)
        PRE_SCRIPT="${1}"
        ;;
    -postScript)
        POST_SCRIPT="${1}"
        ;;
    -scriptPath)
        SCRIPT_PATH="${1}"
        ;;
    -recursive)
        RECURSIVE="-recursive"
        ;;

    -h | \? | --help)
        help
        ;;
    -?)
        printf 'WARN: Unknown option (ignored): %s\n' "$1" >&2
        help
        ;;
    *)
        if [ -z "${1+x}" ]; then
            # help
            break
        else

            TARGET_FILES+="${1} "
            printf "%b\n" "\e[32mAdded '${1-}' as analysis target.\e[0m"
        fi
        #help
        # exit 0
        # break
        ;;
    esac
    if [ -z "${1+x}" ]; then
        break
    fi
    shift
done
# No quotes here to pass targets as own arguments
"${__headless_path}" "${__projects_path}" ANewProject -readOnly "${PRE_SCRIPT+x}" "${POST_SCRIPT+x}" "${SCRIPT_PATH+x}" "${RECURSIVE+x}" -import ${TARGET_FILES}

#$__headless_path
