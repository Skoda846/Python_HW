from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self, item_ids):
        wait = WebDriverWait(self.driver, 10)

        for item_id in item_ids:
            item_element = wait.until(
                EC.element_to_be_clickable((By.ID, item_id))
            )
            item_element.click()

    def go_to_cart(self):
        cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart.click()
