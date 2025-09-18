#!/bin/bash
set -euxo pipefail

cd "$(dirname "$0")/.."

docker build -f tests/Dockerfile -t design-system-tests .
docker run -i --rm -v "$PWD/tests/screenshots:/design-system/tests/screenshots" -w /design-system design-system-tests
