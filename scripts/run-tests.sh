#!/bin/bash
set -euxo pipefail

cd "$(dirname "$0")/.."

docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f tests/Dockerfile -t design-system-tests .
docker run --rm --ipc=host \
  -v "$(pwd)/tests/screenshots:/design-system/tests/screenshots" \
  -w /design-system \
  design-system-tests
