from data.users import user_1, user_2
from homeworke_5.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_student_registration_form():
    # GIVEN
    registration_page.open()

    # WHEN
    registration_page.fill_first_name(user_1.first_name)
    registration_page.fill_last_name(user_1.last_name)

    registration_page.fill_email(user_1.email)

    registration_page.fill_gender()
    registration_page.fill_number(user_1.number)
    registration_page.fill_date()
    registration_page.fill_subjects(user_1.subjects)
    registration_page.fill_hobbies()
    registration_page.upload_photo(user_1.photo)
    registration_page.current_address(user_1.current_address)
    registration_page.fill_state(user_1.state)
    registration_page.fill_city(user_1.city)

    registration_page.button_submit()

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
