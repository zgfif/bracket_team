from applib.events_urls import EventsUrls
from applib.browser import Browser
from applib.event_data import EventData
from applib.xlsx_file import XlsxFile


def main():
    live_and_upcoming_events_urls = EventsUrls(start_date='2024-12-31', 
                                            end_date='2025-12-30').extract()

    completed_events_urls = EventsUrls(type='completed', 
                                    start_date='2024-12-31', 
                                    end_date='2025-12-30').extract()

    browser = Browser()

    all_events_urls = live_and_upcoming_events_urls + completed_events_urls

    for i, url in enumerate(all_events_urls):
        browser.open(url=url)

        data = EventData(driver=browser.driver).extract()

        browser.logger.info('Event Number %d :', i)
        browser.logger.info(data)

        file = XlsxFile(filepath='total.xlsx')
        
        file.add_row(data)

    browser.driver.close()

# live and upcoming 16 pages. 15 per 10 and 16th - 1.
# completed 88 pages. 87 per 10 and 88th - 9.


if __name__ == '__main__':
    main()
