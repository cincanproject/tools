#!/usr/bin/env bash

# MIT License

# Copyright (c) 2019 Niklas Saari / CinCan Project

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

# set -o xtrace
# Exit script if command fails
# set -o errexit
# Exit if script attempts to use undeclared variables
set -o nounset

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file})"
__root="$(cd "$(dirname "${__dir}")" && pwd)"

help() {
    echo ""
    echo -e "  \e[93mGhidra Headless Decompiler."
    echo -e "  "
    echo -e "  Some of the options have been disabled from original script\n due to being unusable or not useful the with container.\e[0m"
    echo ""
    echo "  USAGE: decompile [<optional args>] INPUT_FILE"
    echo ""
    echo "      [-preScript <ScriptName>] - name of the pre-script. Expected to be located on Ghidra's default location."
    echo "      [-postScript <ScriptName>] - name of the post-script. Expected to be located on Ghidra's default location."
    echo "      [-scriptPath \"<path1>[;<path2>...]\"] - Path(s) of the possible external scripts. Seperate multiple paths with semicolon."
    echo "      [-recursive] - analyze given directory recursively."
    echo "      [-processor <languageID>] - give processor languageID manually instead of detecting automatically. "
    echo "      [-cspec <compilerSpecID>] - give compilerID instead of using default. -processor paramater required with this option."
    echo "      "
    echo "      [-debug] - enable debugging for this scripts (set -o xtrace for this script)"
    echo ""
    exit 0
}

subcommand_help() {

    echo ""
    echo ""
    echo -e "  \e[93mThis is shell script wrapper around 'Ghidra Headless Analyzer'."
    echo -e "  It attemps to provide some default options for easier analysis from Docker container."
    echo -e "  Some of the options have been disabled due to being unusable within container.\e[0m"
    echo ""
    echo -e "  There is a set of additional utilities for helping for defining possible arguments."

    echo "  USAGE: <command> [<optional args>]"
    echo ""
    echo "  list - can be used to list supported processors and available scripts from container. Following args can be used:"
    echo "     processors - list all supported processor architectuers, their variants and supported compilers."
    echo "     compilers - list of supported known compilers for each processor variant."
    echo "     scripts - list all available decompiler scrips."
    echo ""
    echo "  decompile - decompile into the C code and/or make analysis based on post-scripts with given set of configurations or pre-script."
    echo "     see decompile --help for more instructions"
    echo ""

    exit 0
}

list_processors() {
    echo ""
    echo -e "  Supported processor architectures.\n  Run 'list processor <architecture> to see variants/languageID's "
    echo ""
    find "${GHIDRA_HOME}/Ghidra/Processors" -mindepth 1 -maxdepth 1 -printf "\t%-15f\n" | sort
    echo ""
    exit 0
}

search_process_compiler_info() {

    xpath_query="language_definitions/language/${search_param}"
    # See information about location of specs in here: https://ghidra.re/ghidra_docs/analyzeHeadlessREADME.html#processor
    info="$(find "${GHIDRA_HOME}/Ghidra/Processors/${PROCESSOR}/data/languages" -mindepth 1 -maxdepth 1 -name "*.ldefs" -exec xmllint --xpath "${xpath_query}" {} \; 2>/dev/null)"
    #  find "${GHIDRA_HOME}/Ghidra/Processors/x86/data/languages" -mindepth 1 -maxdepth 1 -name "*.ldefs" -exec xmllint {} \;
    #  find "${GHIDRA_HOME}/Ghidra/Processors/x86/data/languages" -mindepth 1 -maxdepth 1 -name "*.ldefs" -exec xmllint --xpath "language_definitions/language/@id" {} \; | tr -d "\n" | sed 's/id/\nid/g'

    # )"
    #echo "$info"
    #     awk -F"=" '{print $2}' |
    #     tr -d '"' |
    #     sed 's/^/    /'
    #)"
}

list_compilers() {
    search_param="*[self::description or self::compiler]"
    search_process_compiler_info
    # Add spacing between description tags before removing them

    if [ -z "$info" ]; then
        echo ""
        echo "    Selected processor '$PROCESSOR' not found."
    else
        info_formatted="$(echo "$info" | sed 's/<description>/<description>\n  /g' | sed 's/\(<description>\|<\/description>\)/\n/g' | tr -d "<>/" | sed 's/compiler/    /g;s/name=/\n    /g')"
        echo ""
        echo "  Supported compilers for each processor variants and matching compilerSpecID's "
        echo ""
        echo -e "  Compiler(s):"
        echo "$info_formatted"
    fi
    echo ""

    exit 0

}

list_decompiler_scripts() {

    echo ""
    echo "    Current decompiler scripts in the container."
    echo "    See source code from the Ghidra's GitHub:"
    echo "    https://github.com/NationalSecurityAgency/ghidra/tree/master/Ghidra/Features/Decompiler/ghidra_scripts"
    echo ""
    find "${GHIDRA_HOME}/Ghidra/Features/Decompiler/ghidra_scripts/" -mindepth 1 -maxdepth 1 -printf "\t%-15f\n" | sort
    echo ""
    exit 0
}

list_language_ids() {
    search_param="@id"
    search_process_compiler_info

    if [ -z "${info:-}" ]; then
        echo ""
        echo "    Selected processor '$PROCESSOR' not found."
    else

        info_formatted="$(echo "$info" | tr -d "\n" | sed 's/id/\nid/g' | awk -F "=" '{print $2}' | tr -d '"' | sed 's/^/    /')"
        echo ""
        echo "  Supported processor variants and matching languageID's of selected processor:"
        echo ""
        echo -e "    LanguageID(s):"
        echo "$info_formatted"
    fi
    # | sed 's/\(<description>\|<\/description>\)//g' \
    echo ""

    exit 0
}

if [ -z "${GHIDRA_HOME-}" ]; then
    GHIDRA_HOME="/opt/ghidra/ghidra_9.1_PUBLIC"
fi

__headless_path="${GHIDRA_HOME}/support/analyzeHeadless"
__projects_path="${GHIDRA_HOME}/ghidra_projects"

if [ -z "${1:-}" ]; then
    echo ""
    echo "  No arguments given."
    echo "  Please, give at least a file or directory to be analyzed with subcommand 'decompile'."
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
    elif [ "${2-}" = "scripts" ]; then
        list_decompiler_scripts
    elif [ "${2-}" = "compilers" ]; then
        if [ -z "${3-}" ]; then
            echo -e "\n  'complier' requires and argument. (processor name)"
            echo -e "  e.g. 'list compilers x86'"
            list_processors
        else
            PROCESSOR="${3}"
            list_compilers
        fi
        shift
    else
        echo -e "\n  'list' requires and argument."
        subcommand_help
    fi
    ;;
decompile)
    # echo "Decompiling..."
    if [ -z "${2-}" ]; then
        echo -e "\n  Subcommand 'decompile' requires argument(s)."
        help
    fi
    shift
    ;;
*)
    shift
    # ${subcommand} $@
    echo ""
    echo -e "  Error: '$subcommand' is not a known subcommand.\n" >&2
    echo -e "       Run ' --help' for a list of known subcommands.\n" >&2
    exit 1

    ;;
esac

# Define default arguments here, before processing given ones:

# Make projects directory if it does not exist
mkdir -p "${__projects_path}"

# External script as default, print's decompiled code into STDOUT
# Dockerfile copies this script into the correct location
POST_SCRIPT_ENABLED="-postScript"
POST_SCRIPT_NAME="DecompileHeadless.java"
SCRIPT_PATH="-scriptPath"
SCRIPT_PATH_VALUE="\$GHIDRA_HOME/Ghidra/Features/Decompiler/ghidra_scrips/DecompileHeadless.java"
# Empty
TARGET_FILES=""

while [ "$#" -gt 0 ]; do
    # echo "${1}"
    # echo "Case is '$1'"
    case "${1}" in
    # -import)
    #     IMPORT_PATH="${1}"
    #     if [ "$2" ]; then
    #         RECURSIVE="-recursive"
    #         shift
    #     fi;;
    -preScript)
        if [ -z "${2-}" ]; then
            echo -e "\n  -preScript requires an argument."
            help
        else
            PRE_SCRIPT_ENABLED="${1}"
            PRE_SCRIPT_NAME="${2}"
            shift
        fi
        ;;
    -postScript)
        if [ -z "${2-}" ]; then
            echo -e "\n  -postScript requires an argument."
            help
        else
            POST_SCRIPT_ENABLED="${1}"
            POST_SCRIPT_NAME="${2}"
            shift
        fi
        ;;
    -scriptPath)
        if [ -z "${2-}" ]; then
            echo -e "\n  -scriptPath requires an argument."
            help
        else
            SCRIPT_PATH="${1}"
            SCRIPT_PATH_VALUE="${2}"
            shift
        fi
        ;;
    -recursive)
        RECURSIVE="-recursive"
        ;;
    -processor)
        if [ -z "${2-}" ]; then
            echo -e "\n  -processor requires an argument: languageID\n  Run 'list processors' to see available architectures.\n"
            help
        else
            PROCESSOR_ENABLED="${1}"
            PROCESSOR_VALUE="${2}"
            shift
        fi
        ;;
    -cspec)
        if [ -z "${2-}" ]; then
            echo -e "\n  -cspec requires an argument: compilerID\n  Run 'list compliers' to see available architectures.\n"
            help
        else
            CSPEC_ENABLED="${1}"
            CSPEC_VALUE="${2}"
            shift
        fi
        ;;
    -max-cpu)
        if [ -z "${2-}" ]; then
            echo -e "\n  -max-cpu requires an integer argument.\n  Setting max-cpu to 0 or a negative integer is equivalent to setting the maximum number of cores to 1. \n"
            help
        else
            MAX_CPU_DEFINED="${1}"
            MAX_CPU_VALUE="${2}"
            shift
        fi
        ;;

    -debug)
        # Use for debugging, show all commands executed by this script
        set -o xtrace
        ;;
    -h | \? | --help)
        help
        ;;
    -? | -*)
        printf '\n  WARNING: Unknown option (ignored): %s\n' "$1" >&2
        help
        ;;
    *)
        if [ -z "${1:-}" ]; then
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
"${__headless_path}" "${__projects_path}" ANewProject -readOnly \
    "${MAX_CPU_DEFINED:-}" "${MAX_CPU_VALUE:-}" \
    "${PRE_SCRIPT_ENABLED:-}" "${PRE_SCRIPT_NAME:-}" \
    "${POST_SCRIPT_ENABLED:-}" "${POST_SCRIPT_NAME:-}" \
    "${SCRIPT_PATH:-}" "${SCRIPT_PATH_VALUE:-}" \
    "${PROCESSOR_ENABLED:-}" "${PROCESSOR_VALUE:-}"\
    "${CSPEC_ENABLED:-}" "${CSPEC_VALUE:-}"\
     "${RECURSIVE:-}" -import ${TARGET_FILES}

#$__headless_path
