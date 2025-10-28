import os
from pathlib import Path
import pytest

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

@pytest.fixture(scope="session")
def browser_type_launch_args():
    headless = os.getenv("MAF_HEADLESS", "true").lower() != "false"
    return {"headless": headless}

try:
    from pytest_html import extras as html_extras
except Exception:
    html_extras = None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()


    if rep.when != "call" or not rep.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    safe = item.nodeid.replace("::", "__").replace("/", "_").replace("\\", "_")
    png_path = ARTIFACTS / f"{safe}.png"

    try:
        page.screenshot(path=png_path)
    except Exception:
        return

    if html_extras is not None:
        extra_img = html_extras.image(str(png_path))
        rep.extra = getattr(rep, "extra", []) + [extra_img]
