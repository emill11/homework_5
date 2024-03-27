from selene import browser, have, command
import os
import tests
import allure

@allure.title("Successful fill form")
def test_student_registration_form():
    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')

    # WHEN
    with allure.step("fill in full name"):
        browser.element('#firstName').perform(command.js.scroll_into_view).type('Ivan')
        browser.element('#lastName').type('Ivanov')

    with allure.step("fill in email, gender, number"):
        browser.element('#userEmail').type('test@test.test')
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        browser.element('#userNumber').type('1234567890')

    with allure.step("fill in date of birth"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="2000"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('option[value="3"]').click()
        browser.element('div[aria-label="Choose Monday, April 3rd, 2000"]').click()

    with allure.step("fill in Subjects, Hobbies"):
        browser.element('#subjectsInput').type('ma').press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()

    with allure.step("upload Picture"):
        browser.element('label[for="uploadPicture"]').click()
        browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'resources/photo.jpg')))

    with allure.step("Current Address, State and City"):
        browser.element('#currentAddress').type('Street 123')
        browser.element('#react-select-3-input').type('NC').press_enter()
        browser.element('#react-select-4-input').type('De').press_enter()

    with allure.step("press submit"):
        browser.element('#submit').press_enter()

    # THEN
    with allure.step("Check form results"):
        browser.element('.table').all('td').even.should(
            have.texts(
                'Ivan Ivanov',
                'test@test.test',
                'Male',
                '1234567890',
                '03 April,2000',
                'Maths',
                'Sports',
                'photo.jpg',
                'Street 123',
                'NCR Delhi'))
