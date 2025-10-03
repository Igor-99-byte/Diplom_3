from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
        

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
    
    def wait_for_order_in_progress(self, order_number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: any(f'0{order_number}' in order.text for order in 
                            driver.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS))
        )

    def create_order_and_get_number(self):
        main_page = MainPage(self.driver)
        main_page.go_to_site()
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        assert main_page.is_order_modal_visible(), "Модальное окно заказа не открылось"
        
        # Получение номера заказа
        order_number = main_page.get_order_number()
        assert order_number, "Не удалось получить номер заказа"
        
        return order_number