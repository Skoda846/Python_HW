from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object для страницы корзины Saucedemo.
    Предоставляет методы для взаимодействия с корзиной и оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализирует CartPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    def checkout(self):
        """
        Нажимает кнопку оформления заказа (Checkout) в корзине.

        Returns:
            None: Метод не возвращает значение, но переходит на страницу оформления заказа.
        """
        wait = WebDriverWait(self.driver, 10)
        checkout_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()