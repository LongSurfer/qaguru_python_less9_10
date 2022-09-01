import allure
import self as self
from selene.support.conditions import have
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import command, be

from utils import attach


def test_register_student():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    with allure.step('Open students registration form'):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step('Input student data'):
        browser.element('#firstName').type('Alex')
        browser.element('#lastName').type('Evans')
        browser.element('#userEmail').type('my@mail.net')

        gender = browser.all('.custom-radio').element_by(have.exact_text('Male'))
        gender.click()

        phone_number = browser.element('#userNumber').type('0001230067')
        phone_number.click()

        browser.element('#dateOfBirthInput').perform(command.js.set_value('01 January 2000'))

        subject_Comp = browser.element('#subjectsInput')
        subject_Comp.type('Computer').press_enter()

        subject_Eng = browser.element('#subjectsInput')
        subject_Eng.type('English').press_enter()

        hobby_sport = browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Sports'))
        hobby_sport.click()

        hobby_reading = browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Reading'))
        hobby_reading.click()

        address = browser.element('#currentAddress')
        address.type('Indonesia, Bali, Kuta')

        browser.element('#submit').perform(command.js.click)

    with allure.step('Assert'):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)


def test_fail_students_form():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver


    with allure.step('Open students registration form'):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step('Submit blank form'):
        browser.element('#submit').perform(command.js.click)

    with allure.step('Assert'):
        '''
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        '''
        def element_visible_status():

            self.driver.silent = True
            element = browser.element('#example-modal-sizes-title-lg')
            self.driver.silent = False
            if element is None:
                return False
            else:
                return True


    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
