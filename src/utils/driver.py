from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#Creates headless webdriver using webdriver-manager package (to make test suite portable for any environment)
class Driver:
    def create_driver():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        #implicit wait is set to 60 seconds due to the extremely long pageload time for google.com/finance at certain times
        driver.implicitly_wait(60)
        return driver