from enum import Enum


class Locator(Enum):

    # login_page_locators

    url = 'https://andrii-dev.cyberproof.io/'
    login_url_text = 'https://sso8-dev.cyberproof.io/'
    email_input = '//*[@id="username"]'
    password_input = '//*[@id="password"]'
    page_title = '//*[@id="kc-page-title"]'
    auth_form = '//*[@id="kc-form-login"]'
    login_btn = '//*[@id="kc-login"]'
    error_msg = '//*[@class="kc-feedback-text"]'

    # dashboard_page_locators

    dashbords_url = 'https://andrii-dev.cyberproof.io/home/dashboards'
    dashboards = '//*[@class="home-dashboards__cards"]'

    # incident_page_locators

    incident_page_url = 'https://andrii-dev.cyberproof.io/home/incidents'
    incident_grid = '//*[@class="k-grid-aria-root"]'
    create_incident_btn = '//button[contains(text(),"Create incident")]'
    create_incident_form = '//*[@id="cbp-modal-window"]'
    incident_name_input = '//*[@id="cbp-input-1"]'
    incident_description_input = '//*[@id="cbp-input-2"]'
    create_incident_modal_btn = '//*[@class="cbp-btn-primary cbp-btn"]'
    create_incident_modal_title = '//*[@id="cbp-modal-window"]//h4'
    incident_add_name = '//*[@id="cbp-input-1"]'
    incident_add_description = '//*[@id="cbp-input-2"]'
    first_incident = '(//table//tr)[2]'
    create_incident_btn_modal = '//*[@id="cbp-modal-window"]//button[contains(text(), "Create incident")]'
    created_incident_name = '(//table//tr)[2]//td[3]/div'
    incident_list = '//table/tbody/tr'
    incident_name_link = '//table/tbody/tr/td/div/span'
    incident_preview_modal = '//*[@class="cbp-modal-layout cbp-modal-layout--aside"]'
    incident_preview_modal_header = '//*[@class="cbp-modal-layout cbp-modal-layout--aside"]//h4'
    create_incident_form_header = '//*[@id="cbp-modal-window"]//h4'



    #channels_page_locators

    channels_page_url = 'https://andrii-dev.cyberproof.io/home/channels'
    add_new_channel_btn = '//*[@class="cbp-nav-item-content ng-star-inserted"]'
    channels_list = '//*[@class="channel__name"]'
    new_channel_modal_window = '//*[@class="cbp-modal-layout"]'
    channel_name_input = '//*[@id="cbp-input-1"]'
    channel_type_dropdown = '//*[@class="cbp-dropdown-select__fake-input"]'
    public_channel_option = '//select/option[contains(text(), "Public")]'
    channel_save_btn = '//button[contains(text(),"Add")]'
    channels_list_names = '//*[@class="channels-list"]'
    channels_list_n = '//*[@class="channel__name"]'
    channel_new_modal_header ='//*[@id="ng-app"]//h4'
    channel_empty_state_placeholder = '//*[@class="content__view-placeholder fs-9 semi-bold ng-star-inserted"]'








