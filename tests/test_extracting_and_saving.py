import unittest
from applib.events_urls import EventsUrls
from applib.browser import Browser
from applib.event_data import EventData
from applib.xlsx_file import XlsxFile



class TestExtractingAndSaving(unittest.TestCase):
    def test_extract_data_and_save_to_file(self):
        live_and_upcoming_events_urls = EventsUrls().extract()

        browser = Browser()

        for url in live_and_upcoming_events_urls:    
            browser.open(url=url)

            event_data = EventData(driver=browser.driver).extract()

            print(event_data)

            file = XlsxFile(filepath='live_and_upcoming.xlsx')
            
            file.add_row(event_data)

        browser.driver.close()
