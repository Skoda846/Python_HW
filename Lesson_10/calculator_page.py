from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора с задержкой вычислений.
    Предоставляет методы для взаимодействия с элементами калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализирует CalculatorPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        """
        Открывает страницу калькулятора в браузере.

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds):
        """
        Устанавливает задержку вычислений в секундах.

        Args:
            seconds (int или str): Количество секунд задержки.

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
        return self

    def click_button(self, locator):
        """
        Нажимает на кнопку калькулятора по заданному локатору.

        Args:
            locator (tuple): Локатор элемента в формате (By, значение).

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        button = self.driver.find_element(*locator)
        button.click()
        return self

    def click_7(self):
        """
        Нажимает на кнопку с цифрой 7.

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        return self.click_button(self.button_7)

    def click_plus(self):
        """
        Нажимает на кнопку сложения (+).

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        return self.click_button(self.button_plus)

    def click_8(self):
        """
        Нажимает на кнопку с цифрой 8.

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        return self.click_button(self.button_8)

    def click_equals(self):
        """
        Нажимает на кнопку равенства (=).

        Returns:
            CalculatorPage: Текущий экземпляр CalculatorPage для цепочки вызовов.
        """
        return self.click_button(self.button_equals)

    def get_result(self):
        """
        Ожидает вычисления результата и возвращает его.

        Returns:
            str: Результат вычисления, отображаемый на экране калькулятора.
        """
        # Ждём изменения результата в экране (45+ сек)
        WebDriverWait(self.driver, 60).until(
            lambda driver: driver.find_element(*self.screen).text.strip() == "15"
        )
        result_element = self.driver.find_element(*self.screen)
        return result_element.text.strip()
