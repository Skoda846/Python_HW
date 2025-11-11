from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
# Отключаем переводчик — добавь эти опции
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Ввод в поле
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Клик кнопки по ID
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Ждём, пока текст кнопки станет "SkyPro"
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "updatingButton").text == "SkyPro"
    )
    print(driver.find_element(By.ID, "updatingButton").text)  # "SkyPro"

finally:
    driver.quit()
