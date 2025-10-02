from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def go_to_site(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        
    def go_to_login_page(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
    
    def login(self, email, password):
        # Сначала переходим на страницу логина
        self.go_to_login_page()
        # Заполняем форму
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        
    def wait_for_login_success(self):
        # Ждем перехода на главную после успешного логина
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )