import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = (
        r"C:\Users\User\AppData\Local\Mozilla Firefox\firefox.exe"
    )

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    backpack = wait.until(EC.element_to_be_clickable((
        By.ID, "add-to-cart-sauce-labs-backpack"
    )))
    backpack.click()

    tshirt = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    tshirt.click()

    onesie = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie"
    )
    onesie.click()

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout.click()

    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Иванов")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    total = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, ".summary_total_label"
    )))
    total_text = total.text.strip()

    expected_total = "Total: $58.29"
    actual_total = total_text
    assert actual_total == expected_total, (
        f"Ожидали '{expected_total}', получили: '{actual_total}'"
    )
