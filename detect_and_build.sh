#!/bin/bash
for image in $(git diff --name-only HEAD~1|grep -Po "[^.]+(?=/)"|uniq)
do
   echo "Running: docker build -t cincan/$image:latest $image/."
   docker build -t cincan/$image:latest $image/.
   
   echo "Running: docker push cincan/$image:latest"
   docker push cincan/$image:latest
done
