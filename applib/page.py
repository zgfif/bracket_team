from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from applib.event import Event
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from logging import Logger




class Page:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def process(self) -> tuple[tuple, ...]:
        """
        Extracts data from cards and returns it. 
        """
        data = []
        
        events_links = self._events_links_elements()

        if not events_links:
            return tuple(data)

        for i in range(1, len(events_links) + 1):
            nth_event_link_element = self._nth_event_link_element(i)
            
            if not nth_event_link_element:
                self._logger.warning('could not found event link element. Stop extraction from this page.')
                return tuple(data)

            self._logger.info(f'start processing {i} event...')
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
            self._logger.info('Could not found any links on events.')
            return tuple()
            
        return tuple(events_links)



    def _process_event_link(self, event_link: WebElement)  -> tuple:
        """
        Return a dict which contains event data (name, email, sport, location).
        """
        return Event(driver=self._driver, event_link=event_link, logger=self._logger).extract()



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
            self._logger.warning(f'Could not found {n}th element.')
        return None

