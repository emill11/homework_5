from data.users import user_1
from models.pages.registration_page import RegistrationPage
import allure

registration_page = RegistrationPage()


@allure.title("Successful fill form")
def test_student_registration_form():
    with allure.step("Open registrations form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.register(user_1)
    with allure.step("Check form results"):
        registration_page.should_registered_user_with(user_1)
