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


    def process(self) -> tuple:
        """
        Extracts data from cards and returns it. 
        """
        data = []
        events_links = self._collect_events_links()
        if events_links and events_links[0]:
            data = self._process_event_link(events_links[0])
        else:
            print('no event links.')
        return tuple(data)
    

    def _collect_events_links(self) -> tuple[WebElement|None, ...]:
        """
        Return tuple of events links.
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
        event_data = Event(driver=self._driver, event_link=event_link).extract()
        return event_data
