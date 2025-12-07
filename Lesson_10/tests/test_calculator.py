import allure

from Lesson_10.calculator_page import CalculatorPage

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для калькулятора с задержкой вычислений."""

    @allure.title("Тест сложения 7 + 8 с задержкой 45 секунд")
    @allure.description("Проверка корректности операции сложения в калькуляторе с установленной задержкой")
    def test_addition(self, driver) -> None:
        """
        Тест операции сложения с ожиданием результата.

        Args:
            setup_calculator: Фикстура для настройки калькулятора с задержкой.
        """

        page = CalculatorPage(driver)
        page.open().set_delay(45)

        # 7 + 8 =
        page.click_7().click_plus().click_8().click_equals()

        result = page.get_result()
        assert result == "15", f"Ожидали 15, получили: {result}"
