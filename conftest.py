import pytest
import os
from utils.driver_factory import get_driver


@pytest.fixture
def driver():

    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        os.makedirs("screenshots", exist_ok=True)
        file = f"screenshots/{item.name}.png"

        try:
            driver.save_screenshot(file)
            print(f"Screenshot saved: {file}")
        except:
            pass