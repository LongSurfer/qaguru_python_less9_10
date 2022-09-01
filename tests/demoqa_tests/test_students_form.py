import allure
import self as self
from selene.support.conditions import have
from selene.support.shared import browser
from selene import command, be


def test_register_student():
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


def test_negative_students_form():
    with allure.step('Open students registration form'):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step('Submit blank form'):
        browser.element('#submit').perform(command.js.click)

    with allure.step('Assert'):
        def element_visible_status():

            self.driver.silent = True
            element = browser.element('#example-modal-sizes-title-lg')
            self.driver.silent = False
            if element is None:
                return False
            else:
                return True

