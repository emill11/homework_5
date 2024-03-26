from data.users import user_1
from models.pages.registration_page import RegistrationPage
import pytest
# registration_page = RegistrationPage({browser: setup_browser})


@pytest.fixture
def registration_page(setup_browser):
    return RegistrationPage(setup_browser)


def test_student_registration_form(registration_page):
    registration_page.open()
    registration_page.register(user_1)
    registration_page.should_registered_user_with(user_1)
