from homeworke_5.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_student_registration_form():
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')

    registration_page.fill_email('test@test.test')

    registration_page.fill_gender()
    registration_page.fill_number('1234567890')
    registration_page.fill_date()
    registration_page.fill_subjects('ma')
    registration_page.fill_hobbies()
    registration_page.upload_photo('photo.jpg')
    registration_page.current_address('Street 123')
    registration_page.fill_state('NC')
    registration_page.fill_city('De')
    registration_page.fill_submit()

    # THEN
    registration_page.should_registered_user_with(
        'Ivan Ivanov',
        'test@test.test',
        'Male',
        '1234567890',
        '03 April,2000',
        'Maths',
        'Sports',
        'photo.jpg',
        'Street 123',
        'NCR Delhi')

    registration_page.close_submiting_form()
