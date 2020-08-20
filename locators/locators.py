from enum import Enum


class Locator(Enum):
    # login_page_locators

    url = 'https://andrii-dev.cyberproof.io/'
    email_input = '//*[@id="username"]'
    password_input = '//*[@id="password"]'
    page_title = '//*[@id="kc-page-title"]'
    auth_form = '//*[@id="kc-form-login"]'
    login_btn = '//*[@id="kc-login"]'
    error_msg = '//*[@class="kc-feedback-text"]'
    error_msg_txt = 'Invalid username or password.'

    # dashboard_page_locators

    dashbords_url = 'https://andrii-dev.cyberproof.io/home/dashboards'
    dashboards = '//*[@class="home-dashboards__cards"]'




    # incident_page_locators

    incident_page_url = 'https://andrii-dev.cyberproof.io/home/incidents'
    incident_grid = '//*[@class="k-grid-aria-root"]'
    create_incident_btn = '//*[@class="mr-2 mb-2 cbp-btn-secondary cbp-btn"][1]'
    create_incident_form = '//*[@id="cbp-modal-window"]'
    incident_name_input = '//*[@id="cbp-input-7"]'
    incident_description_input = '//*[@id="cbp-input-8"]'
    create_incident_modal_btn = '//*[@class="cbp-btn-primary cbp-btn"]'
    incident_title_counter = '//*[@class="incidents-page-header__count relative ng-star-inserted"]'




