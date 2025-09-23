import os
import signal
import subprocess
import time
from contextlib import contextmanager
from random import randrange

import pytest


@contextmanager
def run_local_server():
    port = randrange(8010, 8100)
    subprocess.Popen(
        "npm run build",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        preexec_fn=os.setsid,
    )
    npm_runner = subprocess.Popen(
        f"npm run watch:eleventy -- --port={port}",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        preexec_fn=os.setsid,
    )
    time.sleep(2)
    assert not npm_runner.poll(), npm_runner.stdout.read().decode("utf-8")
    try:
        yield f"http://localhost:{port}/"
    finally:
        os.killpg(os.getpgid(npm_runner.pid), signal.SIGTERM)


@pytest.fixture(scope="session", autouse=True)
def local_server():
    with run_local_server() as url:
        yield url
