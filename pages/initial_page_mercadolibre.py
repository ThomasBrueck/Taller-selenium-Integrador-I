from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class InitialPageMercadoLibre(BasePage):
    SEARCH_FIELD = (By.NAME, 'as_word')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-search-btn')

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_FIELD, product_name)
        time.sleep(1)
        self.click(self.SEARCH_BUTTON)
