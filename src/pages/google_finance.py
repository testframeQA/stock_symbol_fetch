from selenium.webdriver.common.by import By
from src.utils.data import test_url
from src.locators.locators import Locators as loc

class Finance_Page:
    def go_to_url(driver):
        driver.get(test_url)

    def get_page_title(driver):
        page_title = driver.title
        
        return page_title

    #Loads test_url, locates UI elements in div class for You Might Also Be Interested section, 
    # locates the UI elemnts for each of the six stock symbols, creates empty list, loops through 
    # the symbols elements and captures the value of each as a string
    def get_stock_symbols(driver):
        ymbi_frame = (loc.ymbi_stocks_module_class)
        ymbi_symbol = (loc.ymbi_stock_symbol)
        get_symbols = driver.find_element(*ymbi_frame)
        symbols = get_symbols.find_elements(*ymbi_symbol)
        scraped_symbols = []
        for symbol in symbols:
            scraped_symbols.append(symbol.text)
            
        return scraped_symbols