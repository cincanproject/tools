#!/bin/bash
TAG=${TAG:-latest}
echo -e "\e[4mFollowing has changed:\e[24m"
echo -e "\e[36m $(git diff --name-only HEAD~1|grep -Po "^[^/]+(?=/)"|uniq)\e[39m"

for image in $(git diff --name-only HEAD~1|grep -Po "^[^/]+(?=/)"|uniq)
do
   echo -e "\e[45mRunning: docker build -t cincan/$image:$TAG $image/.\e[49m"
   docker build -t cincan/$image:$TAG $image/.
   
   echo -e "\e[45mRunning: docker push cincan/$image:$TAG\e[49m"
   docker push cincan/$image:$TAG
done
