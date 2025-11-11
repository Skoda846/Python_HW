import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    service = Service(
        r"C:\Users\User\Documents\edgedriver_win64\msedgedriver.exe"
    )
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_form_submission(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.clear()
    last_name.send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.clear()
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.NAME, "e-mail")
    email.clear()
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.NAME, "phone")
    phone.clear()
    phone.send_keys("+7985899998787")

    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.clear()

    city = driver.find_element(By.NAME, "city")
    city.clear()
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.clear()
    country.send_keys("Россия")

    job = driver.find_element(By.NAME, "job-position")
    job.clear()
    job.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.clear()
    company.send_keys("SkyPro")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_div = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_div.get_attribute("class"), (
        "Zip code должен быть красным"
    )

    green_fields = {
        "first-name": "first-name",
        "last-name": "last-name",
        "address": "address",
        "city": "city",
        "country": "country",
        "e-mail": "e-mail",
        "phone": "phone",
        "job-position": "job-position",
        "company": "company"
    }

    for name, div_id in green_fields.items():
        try:
            field_div = driver.find_element(By.ID, div_id)
            assert "alert-success" in field_div.get_attribute("class"), (
                f"Поле {name} должно быть зелёным"
            )
        except Exception:
            print(f"Поле {name} не найдено с ID '{div_id}'")
