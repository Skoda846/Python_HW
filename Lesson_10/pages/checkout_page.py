from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Page Object для страницы оформления заказа Saucedemo.
    Предоставляет методы для заполнения информации о покупателе и перехода к обзору заказа.
    """

    def __init__(self, driver):
        """
        Инициализирует CheckoutPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    def fill_info(self, first_name, last_name, postal_code):
        """
        Заполняет форму информации о покупателе.

        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс покупателя.

        Returns:
            None: Метод не возвращает значение.
        """
        wait = WebDriverWait(self.driver, 10)

        first_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)

    def continue_to_overview(self):
        """
        Нажимает кнопку продолжения (Continue) для перехода к обзору заказа.

        Returns:
            None: Метод не возвращает значение, но переходит на страницу обзора заказа.
        """
        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()