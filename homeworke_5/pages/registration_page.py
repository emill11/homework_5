from selene import command, have, browser
from homeworke_5 import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').perform(command.js.scroll_into_view).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self):
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="2000"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('option[value="3"]').click()
        browser.element('div[aria-label="Choose Monday, April 3rd, 2000"]').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()

    def fill_hobbies(self):
        browser.element('label[for="uploadPicture"]').click()

    def upload_photo(self, value):
        browser.element('#uploadPicture').set_value(resources.path(value))

    def current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def fill_submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(
            self,
            first_name,
            email,
            gender,
            number,
            date,
            subjects,
            hobbies,
            photo,
            address,
            city
    ):
        browser.element('.table').all('td').even.should(
            have.texts(
                first_name,
                email,
                gender,
                number,
                date,
                subjects,
                hobbies,
                photo,
                address,
                city
            )
        )

    def close_submiting_form(self):
        browser.element("#closeLargeModal").double_click()

