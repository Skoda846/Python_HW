from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждём появления третьей картинки по id
    third_image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # Пауза для полной загрузки
    time.sleep(2)

    src_value = third_image.get_attribute("src")
    print(f"Src третьей (award): {src_value}")

finally:
    driver.quit()
