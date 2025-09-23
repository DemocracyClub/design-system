#!/bin/bash
set -euxo pipefail

cd "$(dirname "$0")/.."

docker build -f tests/Dockerfile -t design-system-tests .
docker run --rm -it -v "$PWD/tests/screenshots:/design-system/tests/screenshots" -w /design-system design-system-tests python tests/write_screenshot_baseline.py
