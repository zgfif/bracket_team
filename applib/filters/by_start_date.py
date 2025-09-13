from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep




class ByStartDate:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    
    def apply(self, date: str) -> None:
        """
        Apply filter "start_date".
        """
        start_date_element = self._start_date_element()
        
        if start_date_element:
            self._driver.execute_script("arguments[0].removeAttribute('readonly')", start_date_element)
            sleep(0.5)
            start_date_element.send_keys(date)



    def _start_date_element(self) -> WebElement | None:
        """
        Return start date element. If could not found return None.
        """
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'input[name="startDate"]')
        except Exception:
            self._logger.warning('Could not found start date element. Return None')
