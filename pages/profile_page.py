from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def click_order_history_link(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)
    
    def click_logout_button(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
    
    def get_order_count(self):
        orders = self.find_elements(ProfilePageLocators.ORDER_ITEMS)
        return len(orders)