from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from credentials import URLs

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def go_to_login_page(self):
        self.get(URLs.URL_login)
        
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
    
    def login(self, email, password):
        self.go_to_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        
    def wait_for_login_success(self):
        self.wait_for_url_to_be(URLs.URL_site)