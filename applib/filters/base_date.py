from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep
from applib.pick_date import PickDate



class BaseDate:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    
    def apply(self, date: str) -> None:
        """
        Apply filter by date.
        """
        date_element = self._date_element()
        
        if date_element:
            PickDate(driver=self._driver, date_element=date_element, date=date).perform()
            # self._driver.execute_script("arguments[0].removeAttribute('readonly')", date_element)
            # sleep(0.5)
            # date_element.send_keys(date)



    def _date_element(self) -> WebElement | None:
        """
        Return end date element. If could not found return None.
        """
        try:
            return self._driver.find_element(By.CSS_SELECTOR, f'input[name="{self._date_type()}"]')
        except Exception:
            self._logger.warning('Could not found end date element. Return None.')



    def _date_type(self) -> str:
        """
        It could be startDate or endDate.
        """
        raise ValueError('Redefine this method is child classses.')
