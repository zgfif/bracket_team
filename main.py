from applib.go_pages import GoPages
from applib.event_url import EventUrl
from applib.extract_data import ExtractData
from applib.xlsx_file import XlsxFile


def main():
    live_and_upcoming_events_urls = GoPages(start_date='2024-12-31', 
                                            end_date='2025-12-30').perform()

    completed_events_urls = GoPages(type='completed', 
                                    start_date='2024-12-31', 
                                    end_date='2025-12-30').perform()

    event = EventUrl()

    total = live_and_upcoming_events_urls + completed_events_urls

    for i, url in enumerate(total):
        event.open(url=url)

        data = ExtractData(driver=event.driver).perform()

        event.logger.info('Event Number %d :', i)
        event.logger.info(data)

        file = XlsxFile(filepath='total.xlsx')
        
        file.add_row(data)

    event.driver.close()

# live and upcoming 16 pages. 15 per 10 and 16th - 1.
# completed 88 pages. 87 per 10 and 88th - 9.


if __name__ == '__main__':
    main()
