import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    \"\"\"Тесты авторизации в Saucedemo.\"\"\"
    
    @allure.title("Успешная авторизация с валидными учетными данными")
    @allure.description("Вход в систему с корректным логином и паролем")
    def test_successful_login(self, driver) -> None:
        \"\"\"
        Тест успешной авторизации.
        
        Args:
            driver: Фикстура WebDriver.
        \"\"\"
        login_page = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            driver.get("https://www.saucedemo.com/")
        
        with allure.step("Ввести валидный логин"):
            login_page.enter_username("standard_user")
        
        with allure.step("Ввести валидный пароль"):
            login_page.enter_password("secret_sauce")
        
        with allure.step("Нажать кнопку Login"):
            login_page.click_login()
        
        with allure.step("Проверить успешную авторизацию"):
            inventory_page = InventoryPage(driver)
            assert inventory_page.is_page_loaded(), "Страница инвентаря не загрузилась"

    @allure.title("Неуспешная авторизация с неверным паролем")
    @allure.description("Попытка входа с корректным логином и некорректным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login_wrong_password(self, driver) -> None:
        \"\"\"
        Тест неуспешной авторизации с неверным паролем.
        
        Args:
            driver: Фикстура WebDriver.
        \"\"\"
        login_page = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            driver.get("https://www.saucedemo.com/")
        
        with allure.step("Ввести валидный логин"):
            login_page.enter_username("standard_user")
        
        with allure.step("Ввести неверный пароль"):
            login_page.enter_password("wrong_password")
        
        with allure.step("Нажать кнопку Login"):
            login_page.click_login()
        
        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()
            assert "Username and password do not match" in error_message, \
                f"Ожидалось сообщение об ошибке, получено: {error_message}"


@allure.feature("Работа с корзиной")
@allure.severity(allure.severity_level.CRITICAL)
class TestCart:
    \"\"\"Тесты работы с корзиной товаров.\"\"\"
    
    @allure.title("Добавление товара в корзину")
    @allure.description("Добавление первого товара из списка в корзину")
    def test_add_to_cart(self, driver, login) -> None:
        \"\"\"
        Тест добавления товара в корзину.
        
        Args:
            driver: Фикстура WebDriver.
            login: Фикстура для предварительной авторизации.
        \"\"\"
        inventory_page = InventoryPage(driver)
        
        with allure.step("Получить название первого товара"):
            first_item_name = inventory_page.get_first_item_name()
        
        with allure.step("Добавить первый товар в корзину"):
            inventory_page.add_first_item_to_cart()
        
        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()
        
        with allure.step("Проверить наличие товара в корзине"):
            cart_items = inventory_page.get_cart_items()
            assert first_item_name in cart_items, \
                f"Товар {first_item_name} не найден в корзине"


@allure.step("Проверка отображения элемента")
def verify_element_displayed(element_present: bool, element_name: str) -> None:
    \"\"\"
    Проверяет, отображается ли элемент.
    
    Args:
        element_present (bool): Флаг наличия элемента.
        element_name (str): Название элемента для сообщения об ошибке.
    \"\"\"
    assert element_present, f"Элемент '{element_name}' не отображается"


@allure.step("Проверка текста элемента")
def verify_text(expected: str, actual: str, element_name: str) -> None:
    \"\"\"
    Проверяет соответствие текста элемента ожидаемому значению.
    
    Args:
        expected (str): Ожидаемый текст.
        actual (str): Фактический текст.
        element_name (str): Название элемента для сообщения об ошибке.
    \"\"\"
    assert expected == actual, \
        f"Для элемента '{element_name}' ожидался текст '{expected}', получен '{actual}'"
