#! /bin/bash

if [ -z "${1-}" ]; then
   echo "No sample directory provided. Exiting."
   exit 1
fi

SAMPLES="/home/appuser/$1"
RESULTS="/home/appuser/results/"
CHECK="\e[32m[+]\e[0m"

mkdir -p /home/appuser/results/

for f in "$SAMPLES/"*; do
        echo -e $CHECK" Radare2 is now processing $f ..."
        r2 -c "aaa; agC > $RESULTS/${f##*/}.txt" "$f" < /dev/null
        echo -e $CHECK" Done"
done
