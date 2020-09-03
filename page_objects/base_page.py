import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGGING_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
logging.basicConfig(format='%(asctime)s - %(name)s - [%(levelname)8s] - %(message)s',
                    level=logging.INFO,
                    filename="logfile.txt",
                    filemode="a",
                    datefmt='%d-%b-%y %H:%M:%S'
                    )


class BasePage(object):
    log = logging.getLogger(__name__)
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def load(self, url=None):
        self.log.info(f"Navigating to  {self.url}")
        if not url:
            url = self.url
        self.driver.get(url)
        self.wait_for_url(self.url, wait_time=10)
        return self

    def wait_for_element(self, base_element, wait_time=10):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, base_element)))
            if element:
                self.log.info(f'Element {base_element} was found')
        except:
            self.log.warning(f"Element {base_element} was not found")

    def element_is_present(self, element):
        self.log.info(f"Checking if {element} is present")
        try:
            elem = self.driver.find_element_by_xpath(element)
            if elem:
                self.log.info(f"Element {element} is present on the page")
                return True
        except:
            self.log.info(f"Element {element} is not present on the page")
            return False

    def wait_for_url(self, url, wait_time=10):
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: url in driver.current_url)
        except Exception as e:
            self.log.error(f"Something went wrong: Exception occurred - {str(e)}! URL  {url} is not reachable")
            raise e

    def click(self, element):
        try:
            wait = WebDriverWait(self.driver, 10)
            elem = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            elem.click()
        except Exception as e:
            self.log.info(f"Something went wrong: Exception occurred - {str(e)}! Button {element} is not clickable")

    def get_elements(self, elements):
        try:
            list_l = self.driver.find_elements_by_xpath(elements)
            return list_l
        except Exception as e:
            self.log.error(f"Something went wrong: Exception occurred - {str(e)}! Elements {elements} were not found")

    def get_text_from_element(self, element):
        try:
            elem = self.driver.find_element_by_xpath(element)
            return elem.text
        except Exception as e:
            self.log.info(f"Something went wrong: Exception occurred - {str(e)}! {element} has no text")

    def input_value(self, element, value=None):
        try:
            elem = self.driver.find_element_by_xpath(element)
            elem.send_keys(value)
        except Exception as e:
            self.log.info(f"Something went wrong: Exception occurred - {str(e)}! Input {element} was not found")

    def find_element_by_text(self, element, text):
        elem_l = self.get_elements(element)
        for i in elem_l:
            if text == i.text:
                return True
        self.log.info(f"Element with {text} text is not present on the page")
        return False

    def open_link(self, link):
        try:
            elem = self.driver.find_element_by_link_text(link)
            elem.click()
        except Exception as e:
            self.log.info(f"Something went wrong: Exception occurred - {str(e)}! Cannot open {link} link")

    def wait_for_element_disappear(self, base_element, wait_time=10):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.invisibility_of_element_located((By.XPATH, base_element)))
            if element:
                self.log.info(f'Element {base_element} disappeared')
        except:
            self.log.warning(f"Element {base_element} is still present")

