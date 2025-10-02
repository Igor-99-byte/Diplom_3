from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    def click_order(self, index=0):
        orders = self.find_elements(OrderFeedLocators.ORDER_ITEMS)
        if orders:
            orders[index].click()
    
    def is_order_modal_visible(self):
        try:
            self.wait_for_element_visible(OrderFeedLocators.ORDER_MODAL, timeout=5)
            return True
        except:
            return False
    
    def get_order_count(self):
        orders_2 = self.find_elements(OrderFeedLocators.ORDER_ITEMS)
        return len(orders_2)
    
    def get_total_orders_count(self):
        element = self.find_element(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(element.text)
    
    def get_today_orders_count(self):
        element = self.find_element(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(element.text)
    
    def get_in_progress_orders(self):
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS)
        return [element.text for element in elements]