import pytest
from configurations.credentials import username, password, username1, password1
from conftest import decorator_screenshot
from locators.locators import Locator


@pytest.mark.xfail
@pytest.mark.usefixtures('setup_cyberproof')
@decorator_screenshot
def test_unsuccessful_log_in_to_app(setup_cyberproof):
    """
    This TC checks errors due to unsuccessful login:
        * Navigate to Login page: Login page displayed;
        * Log in to app with incorrect user credentials: error message displayed;
        * Check error message text: Error message text is 'Invalid username or password.'

    """
    driver, page = setup_cyberproof

    # Login to app with incorrect user credentials
    page.login(username1, password1)

    # Waiting for Error message element appears on the page
    page.wait_for_element(Locator.error_msg.value)

    # Initialize error message
    expected_error_msg_txt = 'Invalid username ,password.'

    # Checking if Error message is present on the page
    assert page.element_is_present(Locator.error_msg.value), \
        f"Error message {Locator.error_msg.value} is not present on the page"
    page.log.info(f"Error message {Locator.error_msg.value} is present on the page")

    actual_error_msg_txt = page.get_text_from_element(Locator.error_msg.value)

    # Checking if error message text is as expected
    assert expected_error_msg_txt == actual_error_msg_txt, \
        f"Error message text is not as expected: {expected_error_msg_txt} is not equal to {actual_error_msg_txt}"
    page.log.info(f"Error message text is as expected: {expected_error_msg_txt} is equal to {actual_error_msg_txt}")


@pytest.mark.smoke
@pytest.mark.usefixtures('setup_cyberproof')
@decorator_screenshot
def test_successful_log_in_to_app(setup_cyberproof):
    """
    This TC checks successful login to app:

        * Navigate to login page: login page displayed;
        * Log in to app using prepared user credentials: User logged in;
        * Check if user was redirected to Home page: User was redirected to Home page;
        * Check if Dashboards are present on Home page: Dashboards are present on Home page

    """
    driver, page = setup_cyberproof

    # Login to the app with prepared user credentials
    page.login(username, password)

    # Initialization  of the expected url after user successful login
    expected_url = Locator.dashbords_url.value

    # Waiting for Home page loading
    page.wait_for_url(Locator.dashbords_url.value)

    # Initialization of the current Url which we get after login
    current_url = driver.current_url

    # Checking if user was redirected to the Home page when he successfully logged in
    assert expected_url == current_url, f"got wrong url {current_url}, instead of {expected_url}"
    page.log.info(f'User was redirected to Home page {current_url}')

    # Checking if Dashboards are present on the Home page
    assert page.element_is_present(Locator.dashboards.value), \
        f"Dashboards {Locator.dashboards.value} are not displayed on the Home page"
    page.log.info(f"Dashboards {Locator.dashboards.value} are displayed on the Home page")
