from data.users import user_1
from models.pages.registration_page import RegistrationPage
import allure

registration_page = RegistrationPage()


@allure.title("Successful fill form")
def test_student_registration_form():
    registration_page.open()
    registration_page.register(user_1)
    registration_page.should_registered_user_with(user_1)
