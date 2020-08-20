from configurations.web_driver import driver
from configurations.credentials import username, password, username1, password1
from page_objects.login_page import LoginPage
from locators.locators import Locator


class TestLoginToApp:

    # def tear_down_method(self):

    def test_unsuccessful_log_in_to_app(self):
        """
        This TC checks errors due to unsuccessful login:
            * Navigate to Login page: Login page displayed;
            * Log in to app with incorrect user credentials: error message displayed;
            * Check error message text: Error message text is 'Invalid username or password.'
        """

        # Initialization of login page - as a result we get login page window
        page = LoginPage()

        # Loading of the Login page
        page.load(Locator.url.value)

        # Login to app with incorrect user credentials
        page.login(username1, password1)

        # Waiting for Error message element appears on the page
        page.wait_for_element(Locator.error_msg.value)

        # Checking if Error message is present on the page
        page.element_is_present(Locator.error_msg.value)

        # Initialization of Error element
        text = driver.find_element_by_xpath(Locator.error_msg.value)

        # Checking if Error element is present on the page
        assert Locator.error_msg_txt.value in driver.page_source

        # Checking if error message text is as expected
        assert Locator.error_msg_txt.value in text.text

    def test_successful_log_in_to_app(self):
        """
        This TC checks successful login to app:

            * Navigate to login page: login page displayed;
            * Log in to app using prepared user credentials: User logged in;
            * Check if user was redirected to Home page: User was redirected to Home page;
            * Check if Dashboards are present on Home page: Dashboards are present on Home page

        """
        # Initialization of the Login page
        page = LoginPage()

        # Loading of the Login page
        page.load(Locator.url.value)

        # Login to the app with prepared user credentials
        page.login(username, password)

        # Initialization  of the expected url after user successful login
        expected_url = Locator.dashbords_url.value

        # Waiting for Home page loading
        page.wait_for_url(Locator.dashbords_url.value)

        # Initialization of the current Url which we get after login
        current_url = driver.current_url

        # Finding the dashboards element on the Home page
        dashboards = driver.find_element_by_xpath(Locator.dashboards.value)

        # Checking if user was redirected to the Home page when he successfully logged in
        assert expected_url == current_url, f"got wrong url {current_url}, instead of {expected_url}"
        page.log.info("User successfully logged in")

        # Checking if Dashboards are present on the Home page
        assert dashboards.is_displayed()
        page.log.info("Dashboards are displayed on the Home page")
