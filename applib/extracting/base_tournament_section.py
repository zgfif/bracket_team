from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class BaseTournamentSection:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def _nth_section_element(self, nth: int = 1) -> WebElement|None:
        """
        Return n-th section element. If could not found return None.
        """
        tournament_info_element = self._tournament_info_element()
        
        if not tournament_info_element:
            return None
        
        selector = (By.CSS_SELECTOR, f"p:nth-of-type({nth})")

        try:
            return WebDriverWait(tournament_info_element, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print(f'Could not found {nth}th section element')
            return None



    def _tournament_info_element(self) -> WebElement | None:
        """
        Return string containing: sport, start_date - end_date and location
        """
        selector = (By.CSS_SELECTOR, 'div.tournament-info')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find tournament info element')
            return None
