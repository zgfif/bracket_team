from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from applib.event import Event
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class LiveAndUpcoming:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def process(self) -> tuple[dict|None, ...]:
        """
        Extracts data from cards and returns it. 
        """
        data = []
        
        events_links = self._events_links_elements()

        for i in range(len(events_links)):
            n = i + 1
            nth_event_link_element = self._nth_event_link_element(n)
            
            if not nth_event_link_element:
                print('could not found event link element. Stop extraction.')
                return tuple(data)

            print(f'start processing {n} event...')
            event_data = self._process_event_link(nth_event_link_element)

            data.append(event_data)

        return tuple(data)



    def _events_links_elements(self) -> tuple[WebElement|None, ...]:
        """
        Return a tuple of events links.
        """
        selector = (By.CSS_SELECTOR, 'h4.tournament-info-text')
        
        try:
            events_links = WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_all_elements_located(selector)
            )
        except TimeoutException:
            print('can not find any links on events')
            return tuple()
            
        return tuple(events_links)



    def _process_event_link(self, event_link: WebElement)  -> dict:
        """
        Return a dict which contains event data (name, email, sport, location).
        """
        return Event(driver=self._driver, event_link=event_link).extract()



    def _nth_event_link_element(self, n: int) -> WebElement | None:
        """
        Return n-th event link element. If could not found return None.
        """
        selector = (By.XPATH, f"(//h4[contains(@class, 'tournament-info-text')])[{n}]")

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print(f'Could not found {n}th element.')
        return None

