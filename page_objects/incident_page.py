from selenium.webdriver.common.by import By
from .web_driver import driver
from base_p.base_page import BasePage
from .locators import Locator


class IncidentPage(BasePage):

    def __init__(self):
        super().__init__(driver, Locator.url.value)

    #def create_incident(self):

