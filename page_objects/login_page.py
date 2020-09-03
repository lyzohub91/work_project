from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from locators.locators import Locator


class LoginPage(BasePage):


    def login(self, username, password):
        self.email_input = self.driver.find_element(By.XPATH, Locator.email_input.value)
        self.password_input = self.driver.find_element(By.XPATH, Locator.password_input.value)
        self.page_title = self.driver.find_element(By.XPATH, Locator.page_title.value)
        self.login_btn = self.driver.find_element(By.XPATH, Locator.login_btn.value)
        self.email_input.clear()
        self.email_input.send_keys(username)
        self.password_input.clear()
        self.password_input.send_keys(password)
        self.login_btn.click()

    def load(self, url=None):
        self.log.info(f"Navigating to  {self.url}")
        if not url:
            url = self.url
        self.driver.get(url)
