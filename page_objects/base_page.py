import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGGING_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(message)s",
                    level=logging.INFO,
                    filename="logfile.txt",
                    filemode="a"
                    )


class BasePage(object):
    log = logging.getLogger(__name__)
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def load(self, url=None):
        self.log.info(f"Navigating to  {self.url}")
        if not url:
            url = self.url
        self.driver.get(url)

        return self

    def wait_for_element(self, base_element, wait_time=5):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, base_element)))
            if element:
                self.log.info(f'Element {base_element} was found')
        except:
            raise EnvironmentError("No element found")

    def element_is_present(self, element):
        self.log.info(f"Checking if {element} is present")
        try:
            self.driver.find_element_by_xpath(element)
        except:
            raise EnvironmentError(f"{element} is not present on the page")

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.current_url == url)

    def click(self, element):
        self.driver.find_element_by_xpath(element).click()
        return self
