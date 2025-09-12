from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class Filter:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver


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
        # open filter menu:
        mat_expansion_panel_header_element = self._mat_expansion_panel_header_element()

        if not mat_expansion_panel_header_element:
            return
                
        mat_expansion_panel_header_element.click()

        # process published:
        if not published:
            published_element = self._published_element()
            
            if published_element:
                sleep(0.5)
                published_element.click()

        # process sport element:
        sport_select_element = self._mat_select_element()
        
        if sport_select_element:
            sleep(0.5)
            sport_select_element.click()
            mat_option = self._mat_option_element(sport=sport)
            
            if mat_option:
                sleep(0.5)
                mat_option.click()

        # process start date:
        start_date_element = self._start_date_element()
        if start_date_element:
            self._driver.execute_script("arguments[0].removeAttribute('readonly')", start_date_element)
            sleep(0.5)
            start_date_element.send_keys(start_date)

        # process end date:
        end_date_element = self._end_date_element()
        if end_date_element:
            self._driver.execute_script("arguments[0].removeAttribute('readonly')", end_date_element)
            sleep(0.5)
            end_date_element.send_keys(end_date)

        sleep(10)
        # click search
        search_button_element = self._search_button_element()
        if search_button_element:
            sleep(3)
            search_button_element.click()

        sleep(10)



    def _published_element(self) -> WebElement | None:
        selector = (By.CSS_SELECTOR, 'mat-slide-toggle')
        
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )        
        except Exception:
            print('can not find published element')
            return None


    def _mat_expansion_panel_header_element(self) -> WebElement | None:
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'mat-expansion-panel-header')
        except Exception:
            print('can not find mat-expansion-panel-header')
            return None
        


    def _mat_select_element(self) -> WebElement | None:
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'mat-select')
        except Exception:
            print('can not find mat select element')
            return None


    
    def _mat_option_element(self, sport: str|None) -> WebElement | None:
        if not sport:
            sport = 'None'

        try:
            return self._driver.find_element(By.XPATH, f"//mat-option[contains(., '{sport}')]")
        except Exception:
            print('can not find mat option')
            return None
   


    def _start_date_element(self) -> WebElement | None:
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'input[name="startDate"]')
        except Exception:
            print('can not found start date element.')
            return None



    def _end_date_element(self) -> WebElement | None:
        try:
            return self._driver.find_element(By.CSS_SELECTOR, 'input[name="endDate"]')
        except Exception:
            print('can not found end date element.')
            return None



    def _search_button_element(self) -> WebElement | None:
        try:
            return self._driver.find_element(By.XPATH, f"//button[contains(., 'Search')]")
        except Exception:
            print('can not find mat select element')
            return None
