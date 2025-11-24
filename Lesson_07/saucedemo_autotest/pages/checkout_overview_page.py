from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.strip()
