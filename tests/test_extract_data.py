import unittest
from applib.event_data import ExtractData
from applib.browser import EventUrl




class TestExtractData(unittest.TestCase):

    def test_extract_data(self) -> None:
        url = 'https://bracketteam.com/event/6454/MAIG_2025'

        event = EventUrl()
        event.open(url=url)

        data = ExtractData(driver=event.driver).perform()
