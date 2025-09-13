from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep




class ByEndDate:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    
    def apply(self, date: str) -> None:
        """
        Apply filter "end date".
        """
        start_date_element = self._end_date_element()
        
        if start_date_element:
            self._driver.execute_script("arguments[0].removeAttribute('readonly')", start_date_element)
            sleep(0.5)
            start_date_element.send_keys(date)



    def _end_date_element(self) -> WebElement | None:
        """
        Return end date element. If could not found return None.
        """
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'input[name="endDate"]')
        except Exception:
            self._logger.warning('Could not found end date element. Return None.')
            return None
