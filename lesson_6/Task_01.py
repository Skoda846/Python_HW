from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Клик по синей кнопке
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

    # Ждём зелёную плашку и получаем текст
    green_plate = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    print(green_plate.text)  # Выведет: "Data loaded with AJAX get request."

finally:
    driver.quit()
