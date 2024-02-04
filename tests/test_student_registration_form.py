from selene import browser, have, be, by
import time



def test_student_registration_form():

    browser.config.window_width = 2000
    browser.config.window_height = 1000

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')

    browser.element('#userEmail').type('test@test.test')

    #пол
    browser.element('.custom-control-label').click()

    browser.element('#userNumber').type('1234567890')

    #поле дата рождения
    browser.element('#dateOfBirthInput').click()

    #выбор года
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2000"]').click()

    #выбор месяца
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="3"]').click()

    #выбор дня
    browser.element('div[aria-label="Choose Monday, April 3rd, 2000"]').click()

    #предмет
    browser.element('#subjectsInput').type('maths').press_enter()

    #чекбокс
    browser.element('label[for="hobbies-checkbox-1"]').click()

    #адрес
    browser.element('#currentAddress').type('Street 123')

    #штат
    browser.element('#react-select-3-input').type('NCR').press_enter()

    #город
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    #файл
    browser.element('label[for="uploadPicture"]').click()
    browser.element('#uploadPicture').send_keys('C:/file_test/photo-44.jpg')

    browser.element('#submit').click()
    time.sleep(20)


























