import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 2000
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()

