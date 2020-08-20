import pytest
from page_objects.incident_page import IncidentPage
from locators.locators import Locator


class TestIncidents:

    @pytest.mark.usefixtures('setup_cyberproof')
    def test_incident_create(self, setup_cyberproof):
        """
        This TC checks if Create incident modal window appears:
            * Navigate to incident page: Incident page displayed;
            * Check if list of incidents is present on Incident page: List of incidents displayed on Incident page;
            * Click create incident button: Create incident button was clicked
            * Check if Create incident modal window displayed: Create incident modal window is displayed
        """
        # Initialize driver and page from setup_cyberproof fixture
        driver, page = setup_cyberproof

        # Recreate page as Incident page
        page = IncidentPage()

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident page loading
        page.wait_for_url(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_grid.value)

        # Initialization of Incident list element
        incident_list = driver.find_element_by_xpath(Locator.incident_grid.value)

        # Checking if list of incidents is present on the Incident page
        assert incident_list.is_displayed()

        # Open Create incident modal window by clicking on Create incident button
        page.click(Locator.create_incident_btn.value)

        # Wait for Create incident modal window
        page.wait_for_element(Locator.create_incident_form.value)
        create_incident_window = driver.find_element_by_xpath(Locator.create_incident_form.value)

        # Checking if Create incident modal window is displayed
        assert create_incident_window.is_displayed()
        page.log.info(f'{Locator.create_incident_form.value} displayed')
