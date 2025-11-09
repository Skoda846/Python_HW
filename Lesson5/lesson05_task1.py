from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Ждать и кликнуть на синюю кнопку по CSS-классу
    wait = WebDriverWait(driver, 10)
    blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
    blue_button.click()

    print("Клик выполнен! 😊")

finally:
    # Закрыть браузер
    driver.quit()
