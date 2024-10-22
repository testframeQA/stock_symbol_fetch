from src.utils.driver import Driver
from src.pages.google_finance import Finance_Page
from src.utils.data import test_data
import pytest

#loads test_url and confirms page's title contains necessary indictor "Google Finance"
def test_confirm_page_title():
    driver = Driver.create_driver()
    Finance_Page.go_to_url(driver)
    title = Finance_Page.get_page_title(driver)
    if "Google Finance" not in title:
        pytest.fail(f"Page Title Missing Expected Text - {title}")
        
#loads test_url, captures stock symbols in YMBI section, compares that set to test_data, prints symbols in YMBI not found in test_data
def test_stock_symbol_ymbi_diff():
    driver = Driver.create_driver()
    Finance_Page.go_to_url(driver)
    ymbi_stocks = Finance_Page.get_stock_symbols(driver)
    print(f"Test Data - {test_data}")
    print(f"YMBI Symbols - {ymbi_stocks}")
    diffs = [symbol for symbol in ymbi_stocks if symbol not in test_data]
    if diffs == None:
        print(f"All Stock Symbols in Google Finance YMBI Section Also Exist In Test Data")
    else:
        print(f"Stock Symbols In Google Finance YMBI Section Not In Test Data - {diffs}")

#loads test_url, captures stock symbols in YMBI section, compares that set to test_data, prints symbols in test_data not found in YMBI section  
def test_stock_symbol_data_diff():
    driver = Driver.create_driver()
    Finance_Page.go_to_url(driver)
    ymbi_stocks = Finance_Page.get_stock_symbols(driver)
    print(f"Test Data - {test_data}")
    print(f"YMBI Symbols - {ymbi_stocks}")
    diffs = [symbol for symbol in test_data if symbol not in ymbi_stocks]
    if diffs == None:
        print(f"All Stock Symbols in Test Data Also Exist In Google Finance YMBI Section")
    else:
        print(f"Stock Symbols In Test Data Not In Google Finance YMBI Section  - {diffs}")

#included this in case suite has to be run with python and not pytest    
if __name__ == "__main__":
    test_confirm_page_title()
    test_stock_symbol_ymbi_diff()
    test_stock_symbol_data_diff()