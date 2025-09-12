from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
from applib.page import Page
from applib.xlsx_file import XlsxFile




class PassPages:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, tabname: str) -> None:
        self._driver = driver
        self._tabname = tabname



    def perform(self) -> None:
        """
        Pass through paginated pages.
        """
        pages_count_element = self._pages_count_element()
        
        if not pages_count_element:
            print('can not find page count element. Stop processing')
            return
        
        pages_count = int(pages_count_element.text.split()[-1])
        
        for i in range(pages_count):
            sleep(10)

            print(f'Processing {i+1} page...')

            data = Page(self._driver).process()

            print(data)
            # add data to file
            XlsxFile('live_and_upcoming.xlsx').add_rows(data)
            
            next_page_button_element = self._next_page_button_element()

            if not next_page_button_element:
                print('can not find next page button element. Stop changing pages.')
                return

            next_page_button_element.click()

        print(f'Congratulations! We have finished processing the tab \'{self._tabname}\'')



    def _pages_count_element(self) -> WebElement | None:
        """
        Return pages count element. If could not found return None.
        """
        selector = (By.XPATH, '/html/body/app-root/app-events/section/div/div/app-pagination/div/div[1]/p[2]')
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found pages count element')
            return
        


    def _next_page_button_element(self) -> WebElement | None:
        """
        Return next page button element. If could not found return None.
        """
        selector = (By.XPATH, '/html/body/app-root/app-events/section/div/div/app-pagination/div/div[1]/button[2]')
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found next page button element')
            return
