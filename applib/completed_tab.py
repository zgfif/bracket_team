from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from logging import Logger
from time import sleep




class CompletedTab:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger
    
    

    def switch(self) -> None:
        """
        Perform switch to the "Competed" tab.
        """
        completed_tab_element = self._completed_tab_element()

        if not completed_tab_element:
            return
        
        try:
            sleep(0.5)
            completed_tab_element.click()
            self._logger.info('Switched to \'Completed\' tab.')
        except Exception:
            self._logger.warning('Could not click on Completed tab element.')
            return
        sleep(15)



    def _completed_tab_element(self) -> WebElement | None:
        """
        Return Completed tab element. If could not found return None.
        """
        selector = (By.XPATH, "//div[contains(text(), 'Completed')]")

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            self._logger.warning('Could not found Completed tab element. Return None.')
