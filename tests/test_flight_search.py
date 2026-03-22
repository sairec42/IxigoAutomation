from pages.flights_page import FlightsPage
from utils.ai_price_analyzer import find_cheapest_flight
from utils.logger import get_logger

logger = get_logger()


def test_search_flights(driver):

    page = FlightsPage(driver)

    logger.info("Opening Flights Tab")
    page.open_flights_tab()

    logger.info("TC1: Origin Chennai")
    page.select_origin("Chennai")

    logger.info("TC2: Destination Mumbai")
    page.select_destination("Mumbai")

    logger.info("TC3: Date selection")
    page.select_date_and_traveller()

    logger.info("TC4: Search flights")
    page.search_flights()

    logger.info("TC5: Get prices")
    prices = page.get_flight_prices()

    assert len(prices) > 0
    logger.info(f"Prices: {prices}")

    logger.info("AI: Find cheapest")
    cheapest = find_cheapest_flight(prices)
    logger.info(f"Cheapest: {cheapest}")

    logger.info("TC6: Open cheapest flight")
    page.open_cheapest_flight(cheapest)

    logger.info("TC7: Validate route")
    route = page.validate_route()

    assert "MAA-BOM" in route