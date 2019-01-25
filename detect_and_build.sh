#!/bin/bash
TAG=${TAG:-latest}
for image in $(git diff --name-only HEAD~1|grep -Po "[^.]+(?=/)"|uniq)
do
   echo "Running: docker build -t cincan/$image:$TAG $image/."
   docker build -t cincan/$image:$TAG $image/.
   
   echo "Running: docker push cincan/$image:$TAG"
   docker push cincan/$image:$TAG
done
