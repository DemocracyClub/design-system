#!/bin/bash
set -euxo pipefail

cd "$(dirname "$0")/.."

docker build -f tests/Dockerfile -t design-system-tests .
docker run --rm -it -u $(id -u):$(id -g) -v "$PWD/tests/screenshots/baseline:/design-system/tests/screenshots/baseline" -w /design-system design-system-tests python tests/write_screenshot_baseline.py
