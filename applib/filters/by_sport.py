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
        Apply filter "sport".
        """
        self._logger.info('Appying filter by kind of sport: \'%s\'...', kind_of_sport)

        sport_select_element = self._sport_select_element()

        if not sport_select_element:
            return

        sleep(0.5)

        try:
            sport_select_element.click()
        except Exception:
            self._logger.exception('Could not click on sport_select element. Stop applying filter sport.')
            return

        sport_option_element = self._sport_option_element(kind_of_sport=kind_of_sport)
        
        if not sport_option_element:
            return
        
        sleep(0.5)

        try:
            sport_option_element.click()
        except Exception:
            self._logger.exception('Could not click on sport_option element. Stop applying filter sport.')
            return



    def _sport_select_element(self) -> WebElement | None:
        """
        Return Sport select element. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'mat-select')

        try:
            return self._driver.find_element(*selector)
        except Exception:
            self._logger.warning('Could not found sport select element. Return None.')


    
    def _sport_option_element(self, kind_of_sport: str|None) -> WebElement | None:
        """
        Return Sport option element with with specific Text. If could not fount return None.
        """
        sport = str(kind_of_sport)

        selector = (By.XPATH, f"//mat-option[contains(., '{sport}')]")

        try:
            return self._driver.find_element(*selector)
        except Exception:
            self._logger.warning('Could not found sport option with \'%s\'. Return None.', sport)
