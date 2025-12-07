from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Page Object для страницы товаров (инвентаря) Saucedemo.
    Предоставляет методы для взаимодействия с товарами и корзиной.
    """

    def __init__(self, driver):
        """
        Инициализирует InventoryPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    def add_items_to_cart(self, item_ids):
        """
        Добавляет товары в корзину по их идентификаторам.

        Args:
            item_ids (list): Список строковых идентификаторов товаров для добавления в корзину.

        Returns:
            None: Метод не возвращает значение.
        """
        wait = WebDriverWait(self.driver, 10)

        for item_id in item_ids:
            item_element = wait.until(
                EC.element_to_be_clickable((By.ID, item_id))
            )
            item_element.click()

    def go_to_cart(self):
        """
        Переходит в корзину, нажимая на иконку корзины.

        Returns:
            None: Метод не возвращает значение, но переходит на страницу корзины.
        """
        cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart.click()