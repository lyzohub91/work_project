import pytest
from conftest import decorator_screenshot
from page_objects.incident_page import IncidentPage
from locators.locators import Locator
from configurations.helpers import get_random_alphanumeric_string



class TestIncidents:

    @pytest.mark.usefixtures('authorization_cyberproof')
    @decorator_screenshot
    def test_incident_create_form(self, authorization_cyberproof):
        """
        This TC checks if Create incident modal window appears:
            * Navigate to incident page: Incident page displayed;
            * Check if list of incidents is present on Incident page: List of incidents displayed on Incident page;
            * Click create incident button and check if create
            incident modal window displayed: Create incident modal window is displayed
        """
        # Initialize driver and page from authorization_cyberproof fixture
        driver, page = authorization_cyberproof

        # Recreate page as Incident page
        page = IncidentPage(driver, Locator.incident_page_url.value)

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_grid.value)

        # Checking if list of incidents is present on the Incidents page
        assert page.element_is_present(Locator.incident_grid.value), \
            f"List of incidents {Locator.incident_grid.value} is not present on the incidents page"
        page.log.info(f"List of incidents {Locator.incident_grid.value} is present on the incidents page")

        # Checking if list of incidents is not empty
        assert page.get_elements(Locator.incident_list.value), \
            f"List of incidents {Locator.incident_list.value} is empty"
        page.log.info(f"List of incidents {Locator.incident_list.value} is not empty")

        # Waiting for Create incident button appears
        page.wait_for_element(Locator.create_incident_btn.value)

        # Checking if create incident button is present on incidents page
        assert page.element_is_present(Locator.create_incident_btn.value), \
            f"Create incident button {Locator.create_incident_btn.value} is not present"
        page.log.info(f"List of incidents {Locator.incident_grid.value} is not empty")

        # Open Create incident modal window by clicking on Create incident button
        page.click(Locator.create_incident_btn.value)

        # Wait for Create incident modal window
        page.wait_for_element(Locator.create_incident_form.value)

        # Checking if Create incident modal window is displayed
        assert page.element_is_present(Locator.create_incident_form.value), \
            f"Create incident modal {Locator.create_incident_form.value} is not displayed"
        page.log.info(f"Create incident modal {Locator.create_incident_form.value} is displayed")

        # Getting the header of Create incident modal window
        name = page.get_text_from_element(Locator.create_incident_modal_title.value)

        # Checking if Create incident modal header is equal to "Create incident"
        expected_value = 'Create incident'

        # Checking if create incident modal header is equal to "Create incident"
        assert name == expected_value, f"Create incident modal header {name} is not equal {expected_value}"
        page.log.info(f"Create incident modal header is {expected_value}")


    @pytest.mark.usefixtures('authorization_cyberproof')
    @decorator_screenshot
    @pytest.mark.smoke
    def test_incident_create(self, authorization_cyberproof):
        """
        This TC checks if Created incident appears on incident list:
            * Navigate to incident page: Incident page displayed;
            * Check if list of incidents is present on Incident page: List of incidents displayed on Incident page;
            * Click create incident button, type incident name and description, click Create incident button:
            New incident appears on incident name
        """

        driver, page = authorization_cyberproof

        # Recreate page as Incident page
        page = IncidentPage(driver, Locator.incident_page_url.value)

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_grid.value)

        # Open create incident form
        page.click(Locator.create_incident_btn.value)

        # Wait for Create incident modal window
        page.wait_for_element(Locator.create_incident_form.value)

        # Wait for incident add name input on Create incident modal
        page.wait_for_element(Locator.incident_add_name.value)

        # Storing new incident name
        expected_name = get_random_alphanumeric_string(10)

        # Typing the incident name to Name field
        page.input_value(Locator.incident_add_name.value, f'{expected_name}')

        # Type incident description
        page.input_value(Locator.incident_add_description.value, f'{get_random_alphanumeric_string(10)}')

        # Click create incident button
        page.click(Locator.create_incident_btn_modal.value)

        # Wait for created incident modal disappears
        page.wait_for_element_disappear(Locator.create_incident_form.value)

        # Checking if create incident modal disappeared
        assert page.element_is_present(Locator.create_incident_form.value) == True, \
            f"Create incident modal {Locator.create_incident_form.value} is still displayed"
        page.log.info(f"Create incident modal {Locator.create_incident_form.value} is not displayed")

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_list.value)

        # Waiting for created incident appears on the page
        page.wait_for_element(Locator.created_incident_name.value)

        # Check if created incident was created and present in the list
        assert page.find_element_by_text(Locator.created_incident_name.value, expected_name), \
            f"Incident was not created, incident with name {expected_name} is not present in the incident list"
        page.log.info(f"Incident with name {expected_name} was created. Incident is present in the list")

        # Check if first incident in the table has created incident name
        assert page.get_text_from_element(Locator.created_incident_name.value) == expected_name, \
            f"First incident with name {expected_name} is not present in the incident list"
        page.log.info(f"Incident with name {expected_name} is present in the list")

    @pytest.mark.usefixtures('authorization_cyberproof')
    @decorator_screenshot
    def test_incident_preview_modal(self, authorization_cyberproof):
        """
        This TC checks if Incident preview modal appears on incident list:
            * Navigate to incident page: Incident page displayed;
            * Check if list of incidents is present on Incident page: List of incidents displayed on Incident page;
            * Click create incident button, type incident name and description, click Create incident button:
            New incident appears on incident name
            * Click on Created incident: Incident preview modal displayed
            * Check header on incident preview modal: Header on incident preview page is the same as incident name
        """

        driver, page = authorization_cyberproof

        # Recreate page as Incident page
        page = IncidentPage(driver, Locator.incident_page_url.value)

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_grid.value)

        # Open create incident form
        page.click(Locator.create_incident_btn.value)

        # Wait for Create incident modal window
        page.wait_for_element(Locator.create_incident_form.value)

        # Wait for incident add name input on Create incident modal
        page.wait_for_element(Locator.incident_add_name.value)

        # Storing new incident name
        expected_name = get_random_alphanumeric_string(10)

        # Typing the incident name to Name field
        page.input_value(Locator.incident_add_name.value, f'{expected_name}')

        # Type incident description
        page.input_value(Locator.incident_add_description.value, f'{get_random_alphanumeric_string(10)}')

        # Click create incident button
        page.click(Locator.create_incident_btn_modal.value)

        # Wait for created incident modal disappears
        page.wait_for_element_disappear(Locator.create_incident_form.value)

        # Checking if create incident modal disappeared
        assert page.element_is_present(Locator.create_incident_form.value) == True, \
            f"Create incident modal {Locator.create_incident_form.value} is still displayed"
        page.log.info(f"Create incident modal {Locator.create_incident_form.value} is not displayed")

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_list.value)

        # Waiting for created incident appears on the page
        page.wait_for_element(Locator.created_incident_name.value)

        # Check if created incident was created and present in the list
        assert page.find_element_by_text(Locator.created_incident_name.value, expected_name), \
            f"Incident was not created, incident with name {expected_name} is not present in the incident list"
        page.log.info(f"Incident with name {expected_name} was created. Incident is present in the list")

        # Check if first incident in the table has created incident name
        assert page.get_text_from_element(Locator.created_incident_name.value) == expected_name, \
            f"First incident with name {expected_name} is not present in the incident list"
        page.log.info(f"Incident with name {expected_name} is present in the list")

        # Check if created incident was created and present in the list
        page.click(Locator.first_incident.value)

        # Wait for preview incident modal window
        page.wait_for_element(Locator.incident_preview_modal.value)

        # Checking if preview incident modal window is displayed
        assert page.element_is_present(Locator.incident_preview_modal.value), \
            f"Incident preview modal is not displayed"
        page.log.info(f"Incident preview modal window is displayed")

        # Getting the header of preview incident modal
        header = page.get_text_from_element(Locator.incident_preview_modal_header.value)

        # Checking if incident preview modal header is the same as incident name
        assert expected_name + '1' == header, \
            f"Incident preview modal header is not the same " \
            f"as incident name, expected {expected_name + '1'}, got {header}"
        page.log.info(f"Preview incident name header is {expected_name}")

    @pytest.mark.xfail
    @pytest.mark.usefixtures('authorization_cyberproof')
    @decorator_screenshot
    def test_incident_create_madal_header(self, authorization_cyberproof):
        """
        This TC checks if Create incident modal header name is "Create new incident":
            * Navigate to incident page and check if create incident button is present
            * Click create incident button: Create incident modal displayed
            * Check header on create incident modal: Header on create incident modal is "Create new incident"
        """

        driver, page = authorization_cyberproof

        # Recreate page as Incident page
        page = IncidentPage(driver, Locator.incident_page_url.value)

        # Navigating to the Incident page
        page.load(Locator.incident_page_url.value)

        # Waiting for Incident list appears on the Incident page
        page.wait_for_element(Locator.incident_grid.value)

        # Checking if "Create incident" button is present
        assert page.element_is_present(Locator.create_incident_btn.value)

        # Open create incident form
        page.click(Locator.create_incident_btn.value)

        # Wait for Create incident modal window
        page.wait_for_element(Locator.create_incident_form.value)

        # Checking if "Create new incident" modal is present
        assert page.element_is_present(Locator.create_incident_form.value)

        # Initialization of expected hmodal header and actual modal header
        page_header_expected = 'Create new incident'
        page_header_actual = page.get_text_from_element(Locator.create_incident_form_header.value)

        # Checking if the header on create incident modal is "Create new incident
        assert page_header_expected == page_header_actual, \
            f"Create incident modal header is not as {page_header_expected}," \
            f" should be {page_header_expected} but got {page_header_actual}"
        page.log.info(f'Create incident modal header is {page_header_expected}')






