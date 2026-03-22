import json
from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():

    config_path = Path(__file__).resolve().parents[1] / "config" / "config.json"

    with open(config_path) as f:
        config = json.load(f)

    options = UiAutomator2Options()

    options.platform_name = config["platformName"]
    options.device_name = config["deviceName"]
    options.automation_name = config["automationName"]
    options.app_package = config["appPackage"]
    options.no_reset = config["noReset"]

    driver = webdriver.Remote(
        command_executor=config["serverURL"],
        options=options
    )

    driver.implicitly_wait(config["implicitWait"])

    driver.activate_app("com.ixigo")

    return driver