import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 70)

    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']")))

    btn_7_xpath = "//span[text()='7']"
    btn_7 = driver.find_element(By.XPATH, btn_7_xpath)
    btn_7.click()

    btn_plus_xpath = "//span[text()='+']"
    btn_plus = wait.until(
        EC.element_to_be_clickable((By.XPATH, btn_plus_xpath))
    )
    btn_plus.click()

    btn_8_xpath = "//span[text()='8']"
    btn_8 = wait.until(
        EC.element_to_be_clickable((By.XPATH, btn_8_xpath))
    )
    btn_8.click()

    btn_equals_xpath = "//span[text()='=']"
    btn_equals = wait.until(
        EC.element_to_be_clickable((By.XPATH, btn_equals_xpath))
    )
    btn_equals.click()

    wait.until(EC.visibility_of_element_located((By.ID, "spinner")))
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
    result_text = result_element.text.strip()

    assert result_text == "15", f"Ожидали '15', получили: '{result_text}'"
