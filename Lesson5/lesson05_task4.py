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
    driver.get("http://the-internet.herokuapp.com/login")

    # Ввести username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Ввести password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Нажать кнопку Login
    login_button = driver.find_element(By.CLASS_NAME, "radius")  # Или By.XPATH: "//button[text()='Login']"
    login_button.click()

    # Ждать и вывести текст зелёной плашки (успешный логин)
    wait = WebDriverWait(driver, 10)
    success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    print("Текст плашки:", success_message.text)

finally:
    # Закрыть браузер
    driver.quit()
