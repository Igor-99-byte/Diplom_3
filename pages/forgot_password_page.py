from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators

class ForgotPasswordPage(BasePage):
    def enter_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)
    
    def click_reset_button(self):
        self.click_element(ForgotPasswordLocators.RESET_BUTTON)
    
    def click_show_password_button(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)
    
    def is_password_field_active(self):
        try:
            self.wait_for_element_visible(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD, timeout=5)
            return True
        except:
            return False