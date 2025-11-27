from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        wait = WebDriverWait(self.driver, 10)
        checkout_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
