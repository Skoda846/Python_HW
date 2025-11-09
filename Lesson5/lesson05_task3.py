from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# Настройка опций Firefox с твоим путём
firefox_options = Options()
firefox_options.binary_location = r"C:\Users\User\AppData\Local\Mozilla Firefox\firefox.exe"

# Настройка драйвера
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Ждать и найти поле ввода (по тегу input для надёжности)
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    # Ввести "Sky"
    input_field.clear()
    input_field.send_keys("Sky")

    # Очистить поле
    input_field.clear()

    # Ввести "Pro"
    input_field.send_keys("Pro")

    print("Ввод выполнен успешно! 😊")

finally:
    # Закрыть браузер
    driver.quit()
