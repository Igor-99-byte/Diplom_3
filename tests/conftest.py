import pytest
from user_data import UserData
import requests
from selenium import webdriver
from urls import URLs, EndUrls
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
    
    driver.get(URLs.URL_site)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user():
    """Фикстура для создания пользователя через API"""
    # Регистрация пользователя
    response = requests.post(
        f"{URLs.URL_base_url}{EndUrls.End_url_register}",
        json={"email": UserData.email, "password": UserData.password, "name": UserData.name}
    )
    token = response.json().get('accessToken')
    
    yield UserData.email, UserData.password, UserData.name, token
    
    # Удаление пользователя после теста
    if token:
        requests.delete(
            f"{URLs.URL_base_url}{EndUrls.End_url_delete}", 
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