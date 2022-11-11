import pytest
import time
import os
import signal
import subprocess
from lighthouse import LighthouseRunner


@pytest.fixture(scope="session", autouse=True)
def npm_start():
    npm_runner = subprocess.Popen(
        "npm start",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        preexec_fn=os.setsid,
    )
    time.sleep(2)
    assert not npm_runner.poll(), npm_runner.stdout.read().decode("utf-8")
    yield npm_runner
    os.killpg(os.getpgid(npm_runner.pid), signal.SIGTERM)


paths_to_test = ["/layout-demo/index.html", "/usage/composition/index.html"]


@pytest.mark.parametrize("path", paths_to_test)
def test_accessibility(path):
    base_url = "http://localhost:8080"
    report = LighthouseRunner(
        f"{base_url}{path}", form_factor="desktop", quiet=True
    ).report
    assert report.score["accessibility"] > 0.9
