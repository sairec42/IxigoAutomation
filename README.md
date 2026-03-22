# ixigo-mobile-automation-framework

## Goal
The primary objective of this project is to automate a complete end-to-end flight booking workflow on the Ixigo Android application. The framework is engineered to handle real-world mobile automation challenges, including dynamic data loading, asynchronous UI updates, and the selection of the most cost-effective travel options through programmatic price analysis.

## Framework Architecture
This project utilizes a structured **Page Object Model (POM)** to ensure a clean separation between test scripts and UI-specific locators. 

**Key Technical Components:**
* **Language**: Python 3.10+
* **Driver**: Appium (UiAutomator2)
* **Test Runner**: Pytest
* **Design Pattern**: Page Object Model (POM)

## Test Case Suite (TC1 - TC7)
The automation suite covers the following functional test cases:
* **TC1**: Input and selection of the Origin city (MAA).
* **TC2**: Input and selection of the Destination city (BOM).
* **TC3**: Interaction with the calendar widget for date selection (March 25).
* **TC4**: Execution of the flight search query.
* **TC5**: Programmatic scraping of all available flight prices from the results screen.
* **TC6**: Identification and selection of the cheapest flight card (Akasa Air @ ₹4,334).
* **TC7**: Validation of the "Review Booking" page to verify route and flight details.

## Setup and Installation
1. **Appium Configuration**: Ensure Appium Server 2.0+ is installed and the `uiautomator2` driver is active.
2. **Environment Setup**: Clone the repository and install the required dependencies:
   ```bash
   pip install -r requirements.txt
