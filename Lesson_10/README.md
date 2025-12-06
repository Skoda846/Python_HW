# Автотесты для проекта Lesson_10

Проект содержит автоматизированные тесты для веб-приложений с использованием Python, Selenium, Pytest и Allure.

## 📁 Структура проекта

\\\
Lesson_10/
├── pages/                    # Page Object Model
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_overview_page.py
├── tests/                   # Тестовые сценарии
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_saucedemo_final.py
├── conftest.py             # Фикстуры Pytest
├── calculator_page.py      # Page Object для калькулятора
├── requirements.txt        # Зависимости Python
├── pytest.ini             # Конфигурация Pytest
└── README.md              # Документация
\\\

## 🚀 Быстрый старт

### Предварительные требования

1. **Python 3.8+** - [Скачать Python](https://www.python.org/downloads/)
2. **Java 8+** (для Allure) - [Скачать Java](https://www.java.com/ru/download/)
3. **Allure CLI** - Инструкция установки ниже

### Установка Allure на Windows

1. **Способ 1: через Scoop**
   \\\powershell
   # Установите Scoop (если нет)
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   irm get.scoop.sh | iex
   
   # Установите Allure
   scoop install allure
   \\\

2. **Способ 2: вручную**
   - Скачайте Allure с [официального сайта](https://github.com/allure-framework/allure2/releases)
   - Распакуйте архив
   - Добавьте путь к \in\ в переменную окружения \PATH\

### Установка зависимостей Python

\\\ash
pip install -r requirements.txt
\\\

## 🧪 Запуск тестов

### Базовый запуск
\\\ash
# Запуск всех тестов с генерацией Allure-отчета
pytest

# Запуск с детальным выводом
pytest -v
\\\

### Запуск конкретных тестов
\\\ash
# Только тесты калькулятора
pytest tests/test_calculator.py -v

# Только тесты Saucedemo
pytest tests/test_saucedemo_final.py -v

# По маркерам (если настроены в pytest.ini)
pytest -m smoke
pytest -m regression
\\\

### Параллельный запуск
\\\ash
# Автоматическое определение количества потоков
pytest -n auto

# Запуск в 2 потока
pytest -n 2
\\\

## 📊 Генерация и просмотр Allure-отчетов

### 1. Генерация HTML-отчета
\\\ash
# Генерация отчета из результатов тестов
allure generate allure-results -o allure-report --clean
\\\

### 2. Просмотр отчета
\\\ash
# Открыть отчет в браузере
allure open allure-report

# Или запустить локальный сервер
allure serve allure-results
\\\

### 3. Просмотр без генерации
\\\ash
# Прямой запуск из результатов
allure serve allure-results
\\\

## 📈 Структура Allure-отчета

Отчет содержит следующие разделы:

- **Dashboard** - общая статистика выполнения
- **Suites** - группировка тестов по наборам
- **Graphs** - графики успешности и длительности
- **Timeline** - временная шкала выполнения
- **Behaviors** - группировка по функциональностям
- **Categories** - категории дефектов

## 🔧 Настройка тестов

### Переменные окружения
\\\ash
# URL тестового окружения
set BASE_URL=https://www.saucedemo.com

# Браузер для тестов (chrome/firefox)
set BROWSER=chrome

# Режим headless
set HEADLESS=true
\\\

### Параметры командной строки
\\\ash
# Запуск в headless режиме
pytest --headless

# Указание базового URL
pytest --base-url=https://demo.example.com

# Указание браузера
pytest --browser=firefox
\\\

## 🐛 Устранение неполадок

### Проблема: Allure не генерирует отчет
**Решение:** Проверьте установку Java
\\\ash
java -version
allure --version
\\\

### Проблема: Не запускаются тесты
**Решение:** Проверьте зависимости
\\\ash
pip list | findstr -i "pytest selenium allure"
\\\

### Проблема: Ошибки импорта модулей
**Решение:** Убедитесь, что вы находитесь в правильной директории
\\\ash
# Из корня проекта
cd Lesson_10
pytest
\\\

## 📝 Документация тестов

Каждый тест содержит:

- **@allure.title** - краткое описание теста
- **@allure.description** - подробное описание
- **@allure.feature** - функциональная принадлежность
- **@allure.severity** - критичность теста
- **@allure.step** - шаги выполнения теста

## 📋 Пример теста
\\\python
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    @allure.title("Успешная авторизация")
    @allure.description("Вход с валидными учетными данными")
    def test_successful_login(self):
        with allure.step("Ввести логин"):
            # код
        with allure.step("Ввести пароль"):
            # код
\\\

## 🤝 Участие в разработке

1. Клонируйте репозиторий
2. Создайте ветку для новой функциональности
3. Напишите тесты
4. Запустите существующие тесты
5. Создайте Pull Request

## 📄 Лицензия

Проект создан для образовательных целей.
