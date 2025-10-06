from urls import URLs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URLs.URL_site
    
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def get(self, url):
        return self.driver.get(url)
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
    
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def wait_for_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )
    
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
    
    def execute_script(self, script, args):
        return self.driver.execute_script(script, args)
    
    def create_action_chains(self):
        return ActionChains(self.driver)
    
    def scroll_to_element(self, element):
        self.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_condition(self, condition, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        return WebDriverWait(self.driver, timeout).until(lambda driver: condition())