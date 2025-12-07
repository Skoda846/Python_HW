"""
Пакет page objects для проекта автотестов Saucedemo и калькулятора.

Содержит классы Page Object Model (POM) для взаимодействия с элементами веб-страниц.
Каждый класс соответствует отдельной странице и инкапсулирует её логику.

Классы:
- LoginPage: Страница авторизации
- InventoryPage: Страница товаров (инвентаря)
- CartPage: Страница корзины
- CheckoutPage: Страница оформления заказа
- CheckoutOverviewPage: Страница обзора заказа
"""

from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage
from .checkout_overview_page import CheckoutOverviewPage

__all__ = [
    'LoginPage',
    'InventoryPage',
    'CartPage',
    'CheckoutPage',
    'CheckoutOverviewPage'
]