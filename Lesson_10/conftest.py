import sys
import os

# Добавляем корневую папку проекта в sys.path
sys.path.append(os.path.join(os.path.dirname(__file__)))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('--headless')  # Если без окна

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()