import unittest
from applib.browser import Browser
from applib.event_data import EventData



class TestEventData(unittest.TestCase):

    def test_extract_data(self) -> None:
        url = 'https://bracketteam.com/event/6454/MAIG_2025'

        browser = Browser()

        browser.open(url=url)

        data = EventData(driver=browser.driver, logger=browser.logger).extract()
