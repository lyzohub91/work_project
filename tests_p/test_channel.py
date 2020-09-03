import pytest
from configurations.helpers import get_random_alphanumeric_string
from conftest import decorator_screenshot
from page_objects.channels_page import ChannelsPage
from locators.locators import Locator


class TestChannels:

    @pytest.mark.usefixtures('authorization_cyberproof')
    @decorator_screenshot
    def test_channel_create_modal(self, authorization_cyberproof):
        """
        This TC checks if Create channel modal window appears:
            * Navigate to Channels page: Channels page displayed;
            * Check if list of channels is present on Channels page: List of channels displayed on Channels page;
            * Click on Add new button and check if create New Channel modal window displayed:
             Create New Channel modal window is displayed
            * Checking if New Channel window header is equal to "New Channel" :
             New Channel header is equal to "New channel"
        """
        # Initialize driver and page from authorization_cyberproof fixture
        driver, page = authorization_cyberproof

        # Recreate page as Channels page
        page = ChannelsPage(driver, Locator.channels_page_url.value)

        # Navigating to the Channels page
        page.load(Locator.channels_page_url.value)

        # Waiting for Channels list appears on the Channels page
        page.wait_for_element(Locator.channels_list.value)

        # Check if list of channels is present on Channels page
        assert page.element_is_present(Locator.channels_list.value), \
            f"List of channels {Locator.channels_list.value} is not present on the page"
        page.log.info(f"{Locator.channels_list.value} List of channels is present")

        # Waiting for Add channel button appears on the Channels page
        page.wait_for_element(Locator.add_new_channel_btn.value)

        # Checking if Add new channel button is present on channels page
        assert page.element_is_present(Locator.add_new_channel_btn.value), \
            f"Add channel button {Locator.add_new_channel_btn.value} is not present"
        page.log.info(f"Add channel button {Locator.add_new_channel_btn.value} is present")

        # Open New Channel modal window by clicking on Add new button
        page.click(Locator.add_new_channel_btn.value)

        # Wait for New channel modal window
        page.wait_for_element(Locator.new_channel_modal_window.value)

        # Checking if Add channel modal window is displayed
        assert page.element_is_present(Locator.new_channel_modal_window.value), \
            f"Add channel {Locator.new_channel_modal_window.value} modal window is not displayed"
        page.log.info(f"Add channel {Locator.new_channel_modal_window.value} modal window is displayed")

        # Getting the header of New Channel modal window
        name = page.get_text_from_element(Locator.channel_new_modal_header.value)

        # Checking if Add new channel modal header is equal to "Add channel"
        expected_value = 'Add channel'
        assert name == expected_value, f"Add new channel modal header {name} is not equal to {expected_value}"
        page.log.info(f"Add new channel modal header {name} is equal to  {expected_value}")


    @pytest.mark.usefixtures('authorization_cyberproof')
    @decorator_screenshot
    def test_create_channel(self, authorization_cyberproof):
        """
                This TC checks if new created channel appears on channels page:
                   * Navigate to incident page: Incident page displayed;
                   * Check if list of channels is present on Channels page: List of Channels displayed on Channels page;
                   * Click add new  button and check if create channel modal window displayed: Create New Channel modal
                    window is displayed
                   * Type channel name, select channel type and click save button. Check if New channel appears on
                    Channels page: New created channel is present on channels page
        """

        # Initialize driver and page from authorization_cyberproof fixture
        driver, page = authorization_cyberproof

        # Recreate page as Channels page
        page = ChannelsPage(driver, Locator.channels_page_url.value)

        # Navigating to the Channels page
        page.load(Locator.channels_page_url.value)

        # Waiting for Channels list appears on the Channels page
        page.wait_for_element(Locator.channels_list.value)

        # Check if list of channels is present on Channels page
        assert page.element_is_present(Locator.channels_list.value), \
            f"List of channels {Locator.channels_list.value} is not present on the page"
        page.log.info(f"{Locator.channels_list.value} List of channels is present")

        # Open New Channel modal window by clicking on Add channel button
        page.click(Locator.add_new_channel_btn.value)

        # Checking if Add channel modal window is displayed
        assert page.element_is_present(Locator.new_channel_modal_window.value),  \
            f"Add channel {Locator.new_channel_modal_window.value} modal window is not displayed"
        page.log.info(f"Add channel {Locator.new_channel_modal_window.value} modal window is displayed")

        # Generating channel name and storing it into expected name variable
        expected_name = get_random_alphanumeric_string(10)

        # Type channel name into channel name input field
        page.input_value(Locator.channel_name_input.value, f'{expected_name}')

        channel_type = "Public"

        # Check if Public type of channel is preselected on Add channel modal window
        assert page.get_text_from_element(Locator.channel_type_dropdown.value) == channel_type, \
            f"Channel type in type field is not {channel_type}"
        page.log.info(f"Channel type in type field is {channel_type}")

        # Creating the channel by clicking on Add button
        page.click(Locator.channel_save_btn.value)

        # Check if Add channel modal window closed when you click Add button
        assert (page.element_is_present(Locator.new_channel_modal_window.value)) == False, \
            f"Add channel modal window {Locator.new_channel_modal_window.value} was not closed "
        page.log.info(f"Add channel modal window {Locator.new_channel_modal_window.value} was closed ")

        # Load channels page
        page.load(Locator.channels_page_url.value)

        # Waiting for channels list appears on channels page
        page.wait_for_element(Locator.channels_list.value)

        # Check if channel's list is present on channels page
        assert page.element_is_present(Locator.channels_list.value), \
            f"Channel's list {Locator.channels_list.value} is not present on channels page"
        page.log.info(f"Channel's list {Locator.channels_list.value} is present on channels page")

        # Checking if created channel is present in the channels list
        assert page.find_element_by_text(Locator.channels_list_n.value, expected_name),\
            f"Created channel with name{expected_name} is not present in channels list"
        page.log.info(f"Created channel with name{expected_name} is present in channels list")
