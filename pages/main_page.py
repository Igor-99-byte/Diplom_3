from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_ITEM)
    
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
    
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
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        constructor = self.find_element(MainPageLocators.ORDER_PLACE)
        
        # Прокручиваем к ингредиенту
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ingredient)
        # Ждем, пока ингредиент станет видимым после прокрутки
        self.wait_for_element_visible(MainPageLocators.INGREDIENT_ITEM)
        
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
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
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
            # Получаем элемент с номером заказа
            number_element = self.find_element(MainPageLocators.ORDER_NUMBER_TEXT)
            order_number = number_element.text.strip()
            
            return order_number
        except Exception as e:
            print(f"Не удалось получить номер заказа: {e}")
            return ""

    def wait_for_modal_closed(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL)
        )