import unittest
from applib.go_pages import GoPages
from applib.event_url import EventUrl
from applib.extract_data import ExtractData
from applib.xlsx_file import XlsxFile



class TestGoPages(unittest.TestCase):
    def test_go_all_pages(self):
        live_and_upcoming_events_urls = GoPages().perform()

        event = EventUrl()

        for url in live_and_upcoming_events_urls:    
            event.open(url=url)

            data = ExtractData(driver=event.driver).perform()

            print(data)

            file = XlsxFile(filepath='live_and_upcoming.xlsx')
            
            file.add_row(data)

        event.driver.close()
