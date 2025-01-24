from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

def create_webdriver():
    options = Options()
    options.add_argument("--headless")  # Ensures Firefox runs in headless mode
    options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    options.add_argument("--no-sandbox")  # Bypass OS security model, required on many cloud platforms

    # Check if specific path setup is required for Replit
    try:
        # Specify the path to the geckodriver explicitly if known to work on Replit
        service = Service(executable_path="/path/to/geckodriver")
        driver = webdriver.Firefox(options=options, service=service)
        logging.info("WebDriver initialized successfully.")
    except Exception as e:
        logging.error("Failed to initialize WebDriver: " + str(e))
        driver = None  # Set driver to None if initialization fails

    return driver

def test_webdriver():
    driver = create_webdriver()
    if driver is None:
        logging.error("WebDriver could not be created. Please check the configuration.")
        return

    try:
        driver.get("https://www.example.com")
        # Perform some actions, e.g., print the title to test if the setup works
        logging.info("Title: " + driver.title)
    except Exception as e:
        logging.error("An error occurred while trying to navigate or interact with the page: " + str(e))
    finally:
        driver.quit()  # Make sure to close the driver
        logging.info("WebDriver session closed.")

# Run the test
test_webdriver()
