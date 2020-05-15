#!/bin/bash
TAG=${TAG:-latest}

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

services:
  - docker:dind

before_script:
  - apk add grep git python3
  - docker login -u "\$DOCKERHUB_USER" -p "\$DOCKERHUB_PASS"
  - pip3 install pip --upgrade && pip3 install pytest && pip3 install .

stages:
  - build-and-test
EOF

echo -e "\e[4mFollowing has changed:\e[24m"
echo -e "\e[36m $(git diff --name-only "$GREEN_MASTER"..HEAD|grep -Po "^[^/]+(?=/)"|uniq)\e[39m"

# Store information if there is no jobs generated
no_jobs_generated_for_pipeline=true

for image in $(git diff --name-only "$GREEN_MASTER"..HEAD|grep -Po "^[^/]+(?=/)"|uniq)
do

  if [ ! -f "$image/Dockerfile" ]
  then
      echo -e "\e[33mNo Dockerfile for: $image.\e[39m"
      continue
  fi

  # Skip whole tool if it is dev version (meaning it has dev-marked tests)
   if [ ! -z $(grep pytest.mark.dev "$image"/*.py) ]; then
    echo -e "\e[33mTool $image is under development. Skipping....\e[39m"
       continue
  fi

  # Initial checks pass, real jobs exist
  no_jobs_generated_for_pipeline=false

  cat >> ${GENERATED_CONFIG} << EOF

build-and-test-$image:
  stage: build-and-test
  script:
EOF

  # Add testing only in master branch (when tag is latest-stable)
  MASTER_TAG="latest-stable"
  if [ "$TAG" = "$MASTER_TAG" ]; then
    cat >> ${GENERATED_CONFIG} << EOF
    - pytest -sk "not dev" --basetemp=".tmp/" --strict $image
EOF
  fi
  cat >> ${GENERATED_CONFIG} << EOF
    - docker build -t cincan/"$image":"$TAG" "$image"/.
    - docker push cincan/"$image"
    
EOF
done

# Insert dummy job if there is no real jobs to prevent pipeline being invalid
if [ "$no_jobs_generated_for_pipeline" = true ]; then
cat >> ${GENERATED_CONFIG} << EOF
build-and-test-dummy:
  stage: build-and-test
  script:
    - echo -e "This is dummy job to prevent pipeline considered as invalid (because of being jobless)"

EOF
fi

cat ${GENERATED_CONFIG}
