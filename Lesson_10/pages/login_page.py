from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object для страницы авторизации Saucedemo.
    Предоставляет методы для выполнения входа в систему.
    """

    def __init__(self, driver):
        """
        Инициализирует LoginPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    def login(self, username, password):
        """
        Выполняет вход в систему с указанными учетными данными.

        Args:
            username (str): Имя пользователя для авторизации.
            password (str): Пароль пользователя для авторизации.

        Returns:
            None: Метод не возвращает значение, но переходит на главную страницу после успешного входа.
        """
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