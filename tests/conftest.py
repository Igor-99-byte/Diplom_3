import pytest
import random
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = None
    
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()

@pytest.fixture
def registered_user():
    """Фикстура для создания пользователя через API"""
    base_url = "https://stellarburgers.nomoreparties.site/api"
    email = f"test{random.randint(10000, 99999)}@example.com"
    password = "password123"
    name = "Test User"
    
    # Регистрация пользователя
    response = requests.post(
        f"{base_url}/auth/register",
        json={"email": email, "password": password, "name": name}
    )
    token = response.json().get('accessToken')
    
    yield email, password, name, token
    
    # Удаление пользователя после теста
    if token:
        requests.delete(
            f"{base_url}/auth/user", 
            headers={'Authorization': token}
        )

@pytest.fixture
def logged_in_user(driver, registered_user):
    """Фикстура для залогиненного пользователя"""
    email, password, name, token = registered_user
    
    # Переход на страницу логина
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.login(email, password)
    
    return driver, email, password, name, token