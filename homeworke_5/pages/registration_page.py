from selene import command, have
from selene.support.shared import browser

from homeworke_5 import resources


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]').element_by(have.value('Male')).element('..')
        self.number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.year_drop_down = browser.element('.react-datepicker__year-select')
        self.year = browser.element('option[value="2000"]')
        self.month_drop_down = browser.element('.react-datepicker__month-select')
        self.month = browser.element('option[value="3"]')
        self.day = browser.element('div[aria-label="Choose Monday, April 3rd, 2000"]')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element('label[for="hobbies-checkbox-1"]')

        self.upload = browser.element('#uploadPicture')

        self.addres = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')

        self.submit = browser.element('#submit')

        self.element = browser.element('.table').all('td')

    def open(self):
        browser.config.window_width = 1000
        browser.config.window_height = 2000
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.perform(command.js.scroll_into_view).type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_gender(self):
        self.gender.click()

    def fill_number(self, value):
        self.number.type(value)

    def fill_date(self):
        self.date_of_birth_input.click()
        self.year_drop_down.click()
        self.year.click()

        self.month_drop_down.click()

        self.month.click()
        self.day.click()

    def fill_subjects(self, value):
        self.subjects_input.type(value).press_enter()

    def fill_hobbies(self):
        self.hobbies.perform(command.js.scroll_into_view).click()

    def upload_photo(self, value):
        self.upload.set_value(resources.path(value))

    def current_address(self, value):
        self.addres.type(value)

    def fill_state(self, value):
        self.state.type(value).press_enter()

    def fill_city(self, value):
        self.city.type(value).press_enter()

    def button_submit(self):
        self.submit.press_enter()

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
            addres,
            city
    ):
        self.element.even.should(
            have.texts(
                first_name,
                email,
                gender,
                number,
                date,
                subjects,
                hobbies,
                photo,
                addres,
                city
            )
        )
