from selenium.webdriver.common.by import By
import time
from .base_page import BasePage
    
class InitialPageWikipedia(BasePage):
    SEARCH_FIELD = (By.ID, 'searchInput')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.cdx-search-input__end-button')

    def search_article(self, title):
        self.enter_text(self.SEARCH_FIELD, title)
        time.sleep(1)
        self.click(self.SEARCH_BUTTON)

    def article_title(self):
        title = self.find_element((By.ID, 'firstHeading')).text
        return title

