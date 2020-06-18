#!/bin/bash
TAG=${TAG:-latest}
DEV_TAG="dev"
MASTER_TAG="latest-stable"
STABLE_DIR="stable"
DEV_DIR="development"


echo "$CI_COMMIT_BRANCH"

# Exit on fail immediately
set -e

if [ ! -f GREEN_MASTER_COMMIT.txt ];then
    echo "Cache file not found, should be fixed manually"
    exit 1

else
    echo "Cache file found."
    GREEN_MASTER="$(cat GREEN_MASTER_COMMIT.txt)"
    echo "Latest commit with passed pipeline: $GREEN_MASTER"
fi


GENERATED_CONFIG=${1}
if [ -z "$1" ]; then
    GENERATED_CONFIG="generated-config.yml"
fi

cat >> ${GENERATED_CONFIG} << EOF
image: docker:stable

variables:
  DOCKER_HOST: tcp://docker:2375/

services:
  - docker:dind

before_script:
  - apk add grep git py3-pip python3
  - docker login -u "\$DOCKERHUB_USER" -p "\$DOCKERHUB_PASS"
  - pip3 install pip --upgrade && pip3 install tox && pip3 install . && pip3 install cincan-registry

stages:
  - build-and-test
EOF

echo -e "\e[4mFollowing has changed:\e[24m"
echo -e "\e[36m $(git diff --name-only "$GREEN_MASTER"..HEAD|grep -Po "^[^/]+(?=/)"|uniq)\e[39m"

# Store information if there is no jobs generated
NO_JOBS_GENERATED_FOR_PIPELINE=true

# Check diff for tools in 'stable' folder

for image in $(git diff --name-only "$GREEN_MASTER"..HEAD $STABLE_DIR |grep -Po "^[$STABLE_DIR/]+[^/]+(?=/)"|uniq)
do
  echo "$image"
  name=$(echo "$image" | cut -d "/" -f2)
  if [ ! -f "$image/Dockerfile" ]
  then
      echo -e "\e[33mNo Dockerfile for: $name.\e[39m"
      continue
  fi
  # Initial checks pass, real jobs exist
  NO_JOBS_GENERATED_FOR_PIPELINE=false
  cat >> ${GENERATED_CONFIG} << EOF

build-and-test-$name-stable:
  stage: build-and-test
  script:
EOF

  # Add testing and readme update only in master branch (when tag is latest-stable)
    cat >> ${GENERATED_CONFIG} << EOF
    - tox $image
    - docker build -t "cincan/$name:$TAG" -t "cincan/$name:latest" "$image"/.
EOF
  if [ "$TAG" = "$MASTER_TAG" ]; then
  cat >> ${GENERATED_CONFIG} << EOF
    - docker push cincan/"$name"
    - cincanregistry --tools . utils update-readme -n "$name"
    
EOF
  fi
done

# Check diff for tools in 'development' folder

for image in $(git diff --name-only "$GREEN_MASTER"..HEAD $DEV_DIR |grep -Po "^[$DEV_DIR/]+[^/]+(?=/)"|uniq)
do

  name=$(echo "$image" | cut -d "/" -f2)
  if [ ! -f "$image/Dockerfile" ]
  then
      echo -e "\e[33mNo Dockerfile for: $name.\e[39m"
      continue
  fi

  # Initial checks pass, real jobs exist
  NO_JOBS_GENERATED_FOR_PIPELINE=false

  cat >> ${GENERATED_CONFIG} << EOF

build-and-test-$name-dev:
  stage: build-and-test
  script:

EOF

  # Run test and build in all cases
    cat >> ${GENERATED_CONFIG} << EOF
    - tox "$image"
    - docker build -t cincan/"$name":"$DEV_TAG" "$image"/.
EOF
  # Pushing development images in 'master' branch
  if [ "$TAG" = "$MASTER_TAG" ]; then
  cat >> ${GENERATED_CONFIG} << EOF
    - docker push "cincan/$name"
    
EOF
  fi
done

# Insert dummy job if there is no real jobs to prevent pipeline being invalid
if [ "$NO_JOBS_GENERATED_FOR_PIPELINE" = "true" ]; then
cat >> ${GENERATED_CONFIG} << EOF
build-and-test-dummy:
  stage: build-and-test
  script:
    - echo -e "This is dummy job to prevent pipeline considered as invalid (because of being jobless)"

EOF
fi

cat ${GENERATED_CONFIG}
