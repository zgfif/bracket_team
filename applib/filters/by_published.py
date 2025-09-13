from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep




class ByPublished:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    
    def apply(self, is_published: bool = True) -> None:
        """
        Apply filter "published" True or False.
        """
        
        # Default state is "published". So we click only if is_published - False.
        if not is_published:
            published_element = self._published_element()
            
            if published_element:
                sleep(0.5)
                published_element.click()

    
    
    def _published_element(self) -> WebElement | None:
        """
        Retunr published element. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'mat-slide-toggle')
        
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )        
        except Exception:
            self._logger.warning('Could not found published element. Return None.')
