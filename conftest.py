from configurations.web_driver import get_driver
import decorator
import allure
import pytest
from page_objects.login_page import LoginPage
from configurations.credentials import username, password
from locators.locators import Locator


def decorator_screenshot(func):
    def wrapper(_, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            driver, _ = args[1]
            allure.attach(driver.get_screenshot_as_png(), name=f"error_{func}.png".format(func.__name__))
            raise
    return decorator.decorator(wrapper, func)


@pytest.fixture(scope="function", autouse=False)
def authorization_cyberproof():
    driver = get_driver()
    driver.maximize_window()
    page = LoginPage(driver, Locator.url.value)
    page.load(Locator.url.value)
    page.login(username, password)
    yield driver, page
    driver.quit()


@pytest.fixture(scope="function", autouse=False)
def setup_cyberproof():
    driver = get_driver()
    driver.maximize_window()
    page = LoginPage(driver, Locator.url.value)
    page.load(Locator.url.value)
    yield driver, page
    driver.quit()
