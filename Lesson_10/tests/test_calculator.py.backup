import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('--headless')  # Если без окна

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.open().set_delay(45)

    # 7 + 8 =
    page.click_7().click_plus().click_8().click_equals()

    result = page.get_result()
    assert result == "15", f"Ожидали 15, получили: {result}"
