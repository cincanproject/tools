#!/bin/bash
TAG=${TAG:-latest}
DEV_TAG="dev"
STABLE_TAG="latest"
# latest-stable to be deprecated in future, use only 'latest' tag in stable tools
MASTER_TAG="latest-stable"
STABLE_DIR="stable"
DEV_DIR="development"


echo "$CI_COMMIT_BRANCH"

# Exit on fail immediately
set -e

if [ -z ${GREEN_MASTER+x} ];then
   # Variable not set

  if [ ! -f GREEN_MASTER_COMMIT.txt ];then
      # File is updated only when the whole pipeline finishes
      echo "Cache file not found or expired. Pass variable with git push options e.g. "
      exit 1 
  else
    echo "Cache file found."
    GREEN_MASTER="$(cat GREEN_MASTER_COMMIT.txt)"
    echo "Latest commit with passed pipeline: $GREEN_MASTER"
  fi
else
  echo "git push option used, latest commit with passed pipeline: $GREEN_MASTER";
fi

GENERATED_CONFIG=${1}
if [ -z "$1" ]; then
    GENERATED_CONFIG="generated-config.yml"
fi

cat >> ${GENERATED_CONFIG} << EOF
image: docker:edge

variables:
  DOCKER_HOST: tcp://docker:2375/

services:
  - docker:dind

before_script:
  - apk add grep git py3-pip python3
  - pip3 install pip --upgrade && pip3 install tox && pip3 install . && pip3 install cincan-registry

EOF
  # Log in only in master branch
  if [ "$CI_COMMIT_BRANCH" = "master" ]; then
  cat >> ${GENERATED_CONFIG} << EOF
  - echo "\$DOCKERHUB_PASS" | docker login -u "\$DOCKERHUB_USER" --password-stdin
  - echo "\$QUAY_PASS" | docker login -u "\$QUAY_USER" quay.io --password-stdin
  - echo "\$GITHUB_PASS" | docker login -u "\$GITHUB_USER" ghcr.io --password-stdin
EOF
  fi
cat >> ${GENERATED_CONFIG} << EOF
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
  name=$(echo "$image" | cut -d "/" -f2)
  if [ ! -f "$image/Dockerfile" ]
  then
      echo -e "\e[33mNo Dockerfile for: $name.\e[39m"
      continue
  fi
  # Initial checks pass, real jobs exist
  NO_JOBS_GENERATED_FOR_PIPELINE=false
  VERSION_TAG=$(grep "tool_version" -m 1 $image/Dockerfile | cut -d "=" -f 2 | tr -d "\"\'()" | sed -e "s/[/ +~]/_/g")
  cat >> ${GENERATED_CONFIG} << EOF

build-and-test-$name-stable:
  stage: build-and-test
  script:
EOF

  # Add testing and readme update only in master branch (when tag is latest-stable)
    cat >> ${GENERATED_CONFIG} << EOF
    - tox $image
    - docker build -t "cincan/$name:$TAG" -t "cincan/$name:$MASTER_TAG" -t "cincan/$name:$VERSION_TAG" -t "quay.io/cincan/$name:$TAG" -t "quay.io/cincan/$name:$VERSION_TAG" -t "ghcr.io/cincanproject/$name:$TAG" -t "ghcr.io/cincanproject/$name:$VERSION_TAG" "$image"/.
EOF
  if [ "$TAG" = "$STABLE_TAG" ]; then
  cat >> ${GENERATED_CONFIG} << EOF
    - docker push cincan/"$name"
    - docker push quay.io/cincan/"$name"
    - docker push ghcr.io/cincanproject/"$name"
    # Update description in Quay and DockerHub
    - cincanregistry --registry Quay --tools . utils update-readme -n "$name"
    - cincanregistry --registry DockerHub --tools . utils update-readme -n "$name"
    
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

  # Run test and build in all cases, suppress error here if no tests
    cat >> ${GENERATED_CONFIG} << EOF
    - tox -- --suppress-no-test-exit-code "$image"
    - docker build -t cincan/"$name":"$DEV_TAG"  -t "quay.io/cincan/$name:$DEV_TAG" -t "ghcr.io/cincanproject/$name:$DEV_TAG" "$image"/.
EOF
  # Pushing development images in 'master' branch
  if [ "$TAG" = "$STABLE_TAG" ]; then
  cat >> ${GENERATED_CONFIG} << EOF
    - docker push "cincan/$name"
    - docker push "quay.io/cincan/$name"
    
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
