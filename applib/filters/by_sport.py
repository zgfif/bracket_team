from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep




class BySport:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    
    def apply(self, kind_of_sport: str | None = None) -> None:
        """
        Apply filter "published" True or False.
        """
                # process sport element:
        sport_select_element = self._mat_select_element()
        
        if sport_select_element:
            sleep(0.5)
            sport_select_element.click()
            mat_option = self._mat_option_element(sport=kind_of_sport)
            
            if mat_option:
                sleep(0.5)
                mat_option.click()



    def _mat_select_element(self) -> WebElement | None:
        """
        Return Mat select element. If could not found return None.
        """
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'mat-select')
        except Exception:
            self._logger.warning('Could not found mat select element. Return None.')


    
    def _mat_option_element(self, sport: str|None) -> WebElement | None:
        """
        Return Mat option element with with specific Text. If could not fount return None.
        """
        if not sport:
            sport = 'None'

        try:
            return self._driver.find_element(By.XPATH, f"//mat-option[contains(., '{sport}')]")
        except Exception:
            self._logger.warning('Could not found mat option with \'%s\'. Return None.', sport)
   