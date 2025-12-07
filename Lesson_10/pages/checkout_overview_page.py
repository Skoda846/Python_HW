from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    """
    Page Object для страницы обзора заказа Saucedemo.
    Предоставляет методы для получения информации о заказе и завершения оформления.
    """

    def __init__(self, driver):
        """
        Инициализирует CheckoutOverviewPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    def get_total_price(self):
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Текст, содержащий итоговую сумму заказа.
        """
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.strip()