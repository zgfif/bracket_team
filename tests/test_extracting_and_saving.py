import unittest
from applib.events_urls import EventsUrls
from applib.browser import Browser
from applib.event_data import EventData
from applib.xlsx_file import XlsxFile
from applib.app_logger import AppLogger


class TestExtractingAndSaving(unittest.TestCase):
    def test_extract_data_and_save_to_file(self):

        app_logger = AppLogger().setup()

        live_and_upcoming_events_urls = EventsUrls(logger=app_logger).extract()

        browser = Browser(logger=app_logger)

        for url in live_and_upcoming_events_urls:    
            browser.open(url=url)

            event_data = EventData(driver=browser.driver, logger=browser.logger).extract()

            print(event_data)

            file = XlsxFile(filepath='live_and_upcoming.xlsx')
            
            file.add_row(tuple(event_data.values()))

        browser.close()
