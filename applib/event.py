from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class Event:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver, event_link: WebElement)  -> None:
        self._driver = driver
        self._event_link = event_link



    def extract(self) -> dict:
        """
        Open the page and extracts data.
        """
        if not self._event_link:
            print('no event link so return empty dict.')
            return {}
        
        name = self._extract_name()
        
        if not self._open_link():
            print('can not open event. return an empty dict')
            return {}

        data = {
            'id': '',
            'name': name,
            'email': self._extract_email(),
            'sport': self._extract_sport(),
            'location': self._extract_location(),
        }

        sleep(5)
        
        self._back_to_cards()

        sleep(5)
        return data



    def _open_link(self) -> bool:
        """
        Open the link.
        """
        try:
            self._event_link.click()
            return True
        except Exception:
            print('can not open the link')
            return False
        


    def _extract_name(self) -> str:
        """
        Return name of event.
        """
        return self._event_link.text



    def _extract_email(self) -> str:
        """
        Return email of event.
        """
        selector = (By.CSS_SELECTOR, "button[mattooltip='Email']")

        try:
            button = WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find email button')
            return ''
        
        sleep(0.5)

        button.click()

        close_selector = (By.XPATH, '//*[contains(@id, "mat-dialog")]/div/div[1]/button')
        try:
            close_modal_button = WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(close_selector)
            )
        except TimeoutException:
            print('Can not find close modal button')
            return ''

        
        email_selector = (By.XPATH, '//*[@class="contact-data" and contains(@href, "mailto")]')

        try:
            email_element = WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(email_selector)
            )
        except TimeoutException:
            print('Can not find email element')
            return ''

        email = email_element.text       

        sleep(2)

        close_modal_button.click()

        return email



    def _extract_sport(self) -> str:
        """
        Return kind of sport.
        """
        tournament_info_element = self._tournament_info_element()
        
        if not tournament_info_element:
            return ''
        
        selector = (By.CSS_SELECTOR, "p:first-of-type")

        try:
            sport_element = WebDriverWait(tournament_info_element, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find sport element')
            return ''
        return  sport_element.text     



    def _extract_location(self) -> str:
        """
        Return the location of event.
        """
        tournament_info_element = self._tournament_info_element()
        
        if not tournament_info_element:
            return ''
        
        selector = (By.CSS_SELECTOR, "p:nth-of-type(3)")

        try:
            location_element = WebDriverWait(tournament_info_element, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find location element')
            return ''
        return location_element.text



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



    def _back_to_cards(self) -> None:
        """
        Return browser to previous page.
        """
        selector = (By.CSS_SELECTOR, 'button.back-button')

        try:
            back_button = WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('can not find back button')
            return
        
        back_button.click()

            