from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep
from applib.filters.by_published import ByPublished
from applib.filters.by_sport import BySport
from applib.filters.by_start_date import ByStartDate
from applib.filters.by_end_date import ByEndDate





class Filter:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def apply(self, 
              published: bool, 
              sport: None|str, 
              start_date: str, 
              end_date: str) -> None:
        """
        Apply filter for events.
        Args:
            published (bool): is published event? (True or False);
            sport (str): possible values [None, Baseball, Basketball, Cornhole, Football, 
                                         Lacrosse, Soccer, Softball, Volleyball, Other];
            start_date: (str): has format mm/dd/yyyy ;
            end_date: (str): has format mm/dd/yyyy .

        """
        self._logger.info('Appying filter: published=%s, sport=%s, start_date=%s, end_date=%s...', 
                          published, sport, start_date, end_date)
        
        self._open_filter_menu()
        
        # Applying filters:
        ByPublished(driver=self._driver, logger=self._logger).apply(is_published=published)

        BySport(driver=self._driver, logger=self._logger).apply(kind_of_sport=sport)

        ByStartDate(driver=self._driver, logger=self._logger).apply(date=start_date)
        sleep(2)
        ByEndDate(driver=self._driver, logger=self._logger).apply(date=end_date)

        sleep(5)
        self._press_search()
        sleep(5)



    def _press_search(self) -> None:
        """
        Click "Search" button.
        """
        search_button_element = self._search_button_element()
        
        if search_button_element:
            sleep(3)
            search_button_element.click()



    def _open_filter_menu(self) -> None:
        """
        Perform opening Filter menu.
        """
        mat_expansion_panel_header_element = self._mat_expansion_panel_header_element()

        if not mat_expansion_panel_header_element:
            return
        mat_expansion_panel_header_element.click()



    def _mat_expansion_panel_header_element(self) -> WebElement | None:
        """
        Return Mat expansion panel header element. If could not found return None.
        """
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'mat-expansion-panel-header')
        except Exception:
            self._logger.warning('Could not found mat-expansion-panel-header. Return None.')



    def _search_button_element(self) -> WebElement | None:
        """
        Return Search button element. If could not found return None.
        """
        try:
            return self._driver.find_element(By.XPATH, f"//button[contains(., 'Search')]")
        except Exception:
            self._logger.warning('Could not found Search button element. Return None.')        
