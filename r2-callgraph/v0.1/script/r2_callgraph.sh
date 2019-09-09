#! /bin/bash

SAMPLES=/r2/samples/*
RESULTS=/r2/results/dot/*
CHECK="\e[32m[+]\e[0m"

mkdir -p /r2/results/dot /r2/results/images

for f in $SAMPLES
do
        echo -e $CHECK" Radare2 is now processing $f ..."
        r2 -c "aa; agCd > /r2/results/dot/${f##*/}.dot" $f < /dev/null
        echo -e $CHECK" Done"
done

for f in $RESULTS
do
        echo -e $CHECK" Generating image from $f ..."
        dot $f -Tpng -o "/r2/results/images/${f##*/}.png"
        echo -e $CHECK" Done"
done
