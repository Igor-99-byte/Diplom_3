from selenium.webdriver.common.by import By

class MainPageLocators:
    # Хедер - кнопка перехода в конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    
    # Хедер - кнопка перехода в ленту заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    
    # Хедер - кнопка перехода в личный кабинет
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    
    # Секция с ингредиентами - карточка ингредиента
    INGREDIENT_ITEM = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    
    # Счетчик на карточке ингредиента (сколько раз добавлен)
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter_num__3nuel']")
    
    # Кнопка "Оформить заказ" в конструкторе
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    
    FLUORESCENT_BUN_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")
    
    # Модальное окно (для деталей ингредиента и номера заказа)
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")

    MODAL_INGRIDIENT = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    
    # Крестик закрытия модального окна
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']")
    
    # Номер заказа в модальном окне после оформления
    ORDER_NUMBER_TEXT = (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")

    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[normalize-space()]")

    ORDER_PLACE = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда (верх)')]")