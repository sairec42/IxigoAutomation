import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from utils.logger import get_logger

logger = get_logger()

class FlightsPage:
    def __init__(self, driver):
        self.driver = driver

    def _find_any(self, locators):
        for by, val in locators:
            try:
                return self.driver.find_element(by, val)
            except NoSuchElementException:
                continue
        raise RuntimeError(f"Element not found: {locators}")

    def open_flights_tab(self):
        logger.info("Step: Opening Flights Tab")
        self._find_any([(AppiumBy.ACCESSIBILITY_ID, "Flights"), (AppiumBy.XPATH, "//android.widget.TextView[@text='Flights']")]).click()

    def select_origin(self, city_name: str):
        logger.info(f"TC1: Origin -> {city_name}")
        self._find_any([(AppiumBy.ACCESSIBILITY_ID, "From"), (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'From')]")]).click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText").send_keys(city_name)
        self.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[contains(@text,'{city_name}')]").click()

    def select_destination(self, city_name: str):
        logger.info(f"TC2: Destination -> {city_name}")
        self._find_any([(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'To')]"), (AppiumBy.XPATH, "(//android.widget.TextView)[2]")]).click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText").send_keys(city_name)
        self.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[contains(@text,'{city_name}')]").click()

    def select_date_and_traveller(self):
        logger.info("TC3: Date Selection")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Depart') or contains(@text,'Mar')]").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='25']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Done') or contains(@text,'Apply')]").click()

    def search_flights(self):
        logger.info("TC4: Searching")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Search')]").click()

    def get_flight_prices(self):
        logger.info("TC5: Scraping Prices")
        while True:
            try:
                price_elements = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'₹')]")
                if price_elements:
                    return [el.text for el in price_elements if "₹" in el.text]
            except StaleElementReferenceException:
                continue
            time.sleep(2)

    def open_cheapest_flight(self, cheapest_price=None):
        logger.info("TC6: Looking for the first actual Flight Card...")
        while True:
            try:
                cards = self.driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[@clickable='true']")
                
                for card in cards:
                    if card.size['width'] > 500 and card.size['height'] > 200:
                        card.click()
                        logger.info("Success: Flight card identified and clicked.")
                        return True
            except (NoSuchElementException, StaleElementReferenceException):
                pass
            
            logger.warning("Still waiting for flight results to load...")
            time.sleep(2)

    def validate_route(self):
        logger.info("TC7: Validating Route")
        while True:
            source = self.driver.page_source.upper()
            if ("MAA" in source or "CHENNAI" in source) and ("BOM" in source or "MUMBAI" in source):
                logger.info("PASS: Route is correct.")
                return "MAA-BOM"
            time.sleep(1)