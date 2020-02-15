#!/bin/bash

function usage() {
    echo -e "usage: '$0 -f <file.eml> -s 800x640'"
    exit 0
}

while getopts "f:s:n:o:h" opt; do
      case $opt in
        f ) MAIL_FILE="$OPTARG";;
        s ) DISPLAY_SIZE="$OPTARG";;
        n ) IMAGE_OUT="$OPTARG";;
        o ) OUTPUT_DIR="$OPTARG";;
        h ) usage;;
        \?) echo "Invalid option: -"$OPTARG"" >&2
            exit 1;;
        : ) echo "Option -"$OPTARG" requires an argument." >&2
            exit 1;;
      esac
done

[ -z "$MAIL_FILE" ] && echo "No .eml file supplied" && exit 1
[ -z "$DISPLAY_SIZE" ] && DISPLAY_SIZE=900x1000
[ -z "$OUTPUT_DIR" ] && OUTPUT_DIR="output"
[ -z "$IMAGE_OUT" ] && IMAGE_OUT="${OUTPUT_DIR}/${MAIL_FILE}.png"

echo ${IMAGE_OUT}

function screenshot_thunderbird() {
    # Sleep on the first screenshot
    if [ $NUM = 0 ]; then
        sleep 5
    fi
    NUM=$((NUM + 1))
    echo "[*] Screenshot #${NUM}"
    mkdir -p ${OUTPUT_DIR}
    TEMP="$(mktemp)"
    (xwd -display :$DISPLAY_NUM -root -out ${TEMP}.xwd >/dev/null &&
        convert ${TEMP}.xwd "${IMAGE_OUT}")
}

export DISPLAY=:99
DISPLAY_NUM=99
SCREEN=0
BIT_DEPTH=24

THUNDERBIRD_PROFILE=/root/thunderbird_profile

echo "[*] Starting Xvfb"
(Xvfb :${DISPLAY_NUM} -screen 0 ${DISPLAY_SIZE}x${BIT_DEPTH} -nolisten tcp) & disown

echo "[*] Starting Headless Thunderbird"
(thunderbird --file ${MAIL_FILE} --profile ${THUNDERBIRD_PROFILE}) & disown

NUM=0
screenshot_thunderbird
