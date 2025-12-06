import allure
import pytest
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    \"\"\"Тесты для калькулятора.\"\"\"
    
    @allure.title("Тест сложения двух чисел")
    @allure.description("Проверка корректности операции сложения в калькуляторе")
    def test_addition(self, setup_calculator) -> None:
        \"\"\"
        Тест операции сложения.
        
        Args:
            setup_calculator: Фикстура для настройки калькулятора.
        \"\"\"
        calculator = setup_calculator
        
        with allure.step("Ввести первое число"):
            calculator.enter_number("5")
        
        with allure.step("Выбрать операцию сложения"):
            calculator.press_operation("+")
        
        with allure.step("Ввести второе число"):
            calculator.enter_number("3")
        
        with allure.step("Нажать кнопку равно"):
            calculator.press_equals()
        
        with allure.step("Проверить результат"):
            result = calculator.get_result()
            assert result == "8", f"Ожидалось 8, получено {result}"

    @allure.title("Тест вычитания двух чисел")
    @allure.description("Проверка корректности операции вычитания")
    def test_subtraction(self, setup_calculator) -> None:
        \"\"\"
        Тест операции вычитания.
        
        Args:
            setup_calculator: Фикстура для настройки калькулятора.
        \"\"\"
        calculator = setup_calculator
        
        with allure.step("Ввести первое число"):
            calculator.enter_number("10")
        
        with allure.step("Выбрать операцию вычитания"):
            calculator.press_operation("-")
        
        with allure.step("Ввести второе число"):
            calculator.enter_number("4")
        
        with allure.step("Нажать кнопку равно"):
            calculator.press_equals()
        
        with allure.step("Проверить результат"):
            result = calculator.get_result()
            assert result == "6", f"Ожидалось 6, получено {result}"


@allure.step("Проверка результата операции")
def verify_calculation_result(actual: str, expected: str) -> None:
    \"\"\"
    Верификация результата вычисления.
    
    Args:
        actual (str): Фактический результат.
        expected (str): Ожидаемый результат.
    \"\"\"
    assert actual == expected, f"Ожидалось {expected}, получено {actual}"
