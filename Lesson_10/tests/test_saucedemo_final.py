from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_total_price_final():
    # Настройка Firefox
    options = Options()
    options.binary_location = (
        r"C:\Users\User\AppData\Local\Mozilla Firefox\firefox.exe"
    )

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    try:
        print("Начало финального теста")

        # Шаг 1: Логин
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        print("Успешный логин")

        # Шаг 2: Добавление товаров
        inventory_page = InventoryPage(driver)

        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        inventory_page.add_items_to_cart(items_to_add)
        print("Товары добавлены в корзину")

        # Шаг 3: Переход в корзину
        inventory_page.go_to_cart()
        print("Перешли в корзину")

        # Шаг 4: Оформление заказа
        cart_page = CartPage(driver)
        cart_page.checkout()
        print("Перешли к оформлению заказа")

        # Шаг 5: Заполнение данных
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("Иван", "Петров", "123456")
        print("Данные заполнены")

        checkout_page.continue_to_overview()
        print("Перешли к итогам")

        # Шаг 6: Проверка итоговой стоимости
        overview_page = CheckoutOverviewPage(driver)
        total_price = overview_page.get_total_price()
        print(f"Итоговая стоимость: {total_price}")

        # Проверка
        assert total_price == "Total: $58.29", (
            f"Expected 'Total: $58.29', but got '{total_price}'"
        )
        print("Test passed!")

    except Exception as e:
        print(f"Test failed: {e}")
        print(f"Current URL: {driver.current_url}")
        driver.save_screenshot("error_final.png")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_total_price_final()
