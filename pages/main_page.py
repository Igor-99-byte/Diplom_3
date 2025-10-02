from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import time

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_order_feed(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        )
        element.click()
    
    def click_personal_account(self):
        acc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        acc.click()
    
    def click_ingredient(self):
        ingredients = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT_ITEM)
        )
        ingredients.click()
    
    def close_modal(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        )
        button.click()
    
    def is_modal_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.MODAL, timeout=5)
            return True
        except:
            return False
    
    def get_ingredient_counter(self):
        counter = self.find_element(MainPageLocators.FLUORESCENT_BUN_COUNTER)
        return int(counter.text)
    
    def add_ingredients_to_order(self):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT_ITEM)
        )
        
        constructor = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_PLACE)
        )
        
        # Прокручиваем к ингредиенту
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ingredient)
        time.sleep(0.5)
        # Перетаскивание: зажать -> переместить -> отпустить
        actions = ActionChains(self.driver)
        (actions
         .move_to_element(ingredient)    # Наводим на ингредиент
         .click_and_hold()               # Зажимаем ЛКМ
         .pause(0.5)                     # Держим зажатым
         .move_to_element(constructor)   # Перемещаем в конструктор
         .pause(0.5)                     # Пауза в конструкторе
         .release()                      # Отпускаем ЛКМ
         .perform())
    
    def click_order_button(self):
        button_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        button_order.click()
    
    def is_order_modal_visible(self):
        try:
            self.wait_for_element_visible(MainPageLocators.MODAL_INGRIDIENT, timeout=10)
            return True
        except:
            return False
    
    def get_order_number(self):
        try:
            # Ждем появления модального окна с номером
            self.wait_for_element_visible(MainPageLocators.ORDER_NUMBER_MODAL, timeout=10)
            time.sleep(3)
            # Получаем элемент с номером заказа
            number_element = self.find_element(MainPageLocators.ORDER_NUMBER_TEXT)
            order_number = number_element.text.strip()
            
            return order_number
        except Exception as e:
            print(f"Не удалось получить номер заказа: {e}")
            return ""