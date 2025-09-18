import json
from urllib.parse import urljoin

import pytest
import os
import subprocess

paths_to_test = ["/layout-demo/index.html", "/usage/composition/index.html"]


@pytest.mark.parametrize(
    "path",
    paths_to_test,
)
def test_accessibility(page, local_server, subtests, path):
    url = urljoin(local_server, path)
    env = os.environ.copy()
    env["CHROME_PATH"] = page.context.browser.browser_type.executable_path
    command = [
        "npx",
        "lighthouse",
        url,
        "--quiet",
        "--chrome-flags=--headless --no-sandbox --disable-setuid-sandbox --disable-gpu --ignore-certificate-errors",
        "--disable-cpu-throttling",
        "--disable-network-throttling",
        "--only-categories='accessibility'",
        "--disable-full-page-screenshot",
        "--output=json",
    ]
    raw_report = subprocess.run(
        command, env=env, check=True, capture_output=True, text=True
    )
    report = json.loads(raw_report.stdout)
    categories = report["categories"]
    audits = report["audits"]

    SCORE_THRESHOLD = 0.99

    for category_key, category_data in categories.items():
        score = category_data.get("score", 1.0)
        category_title = category_data.get("title", category_key)

        # Collect failed audits
        failing_details = []
        for ref in category_data.get("auditRefs", []):
            audit_id = ref["id"]
            audit = audits.get(audit_id)
            if not audit:
                continue
            audit_score = audit.get("score")
            if audit_score is not None and audit_score < SCORE_THRESHOLD:
                title = audit.get("title", audit_id)
                description = audit.get("description", "").strip()
                items = []
                for item in audit.get("details", {}).get("items"):
                    items.append(f"""
                        - {item["node"]["selector"]}:
                            {item["node"]["explanation"]}
                    """)
                failing_details.append(
                    f"- {title}\n  {description}\n {'\n'.join(items)}"
                )

        if score < SCORE_THRESHOLD:
            with subtests.test(msg=f"{category_key} score"):
                detail = (
                    "\n".join(failing_details)
                    if failing_details
                    else "No specific audit failures found."
                )
                raise AssertionError(
                    f"[{category_title}] score was {score}, expected at least {SCORE_THRESHOLD}\n\n"
                    f"Failing audits:\n{detail}\n\n"
                )
