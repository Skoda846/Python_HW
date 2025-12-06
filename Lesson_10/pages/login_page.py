from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(self.driver, 10)

        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()

        # Ждем перехода на главную страницу
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
