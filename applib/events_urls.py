from applib.events_api import EventsApi
from applib.page_parameters import PageParameters
from typing import Type
from logging import Logger


class EventsUrls:
    DEFAULT_EVENT_TYPE = 'live_and_upcoming'
    DEFAULT_START_DATE = '2025-09-01'
    DEFAULT_END_DATE = '2025-09-30'


    def __init__(self,
                 logger: Logger,
                 event_type: str = DEFAULT_EVENT_TYPE, 
                 start_date: str = DEFAULT_START_DATE, 
                 end_date: str = DEFAULT_END_DATE,
                 page_data_cls: Type[EventsApi] = EventsApi,
        ) -> None:
        """
        Collects all event URLs by given criteria (event_type, start_date, end_date).
        """
        self._logger = logger
        self._event_type = event_type
        self._start_date = start_date
        self._end_date = end_date
        self._page_data_cls = page_data_cls

        self._events_urls: list[str] = []
        self._pages_list: list[int] = []
        self._logger.info('Start collecting events urls \'%s\', %s, %s ...', self._event_type, self._start_date, self._end_date)



    def extract(self) -> tuple[str, ...]:
        """
        Return tuple of all events URLs by specific criteria.
        """
        # reset state in case of repeated calls
        self._events_urls.clear()
        self._pages_list.clear()

        # process the first page
        self._process_page(page_number=1)

        # process the rest (if any)
        for page_number in self._pages_list[1:]:
            self._process_page(page_number)

        return tuple(self._events_urls)
    


    def _process_page(self, page_number: int = 1) -> None:
        """
        Process one page: extract pages_list if it's the first page and collect events_urls.
        """
        self._logger.info('Processing page %d', page_number)
        page_data = self._page_data(page_number=page_number)

        page_parameters = PageParameters(data=page_data)

        if page_number == 1:
            self._pages_list = page_parameters.pages_list
        
        self._logger.info('Found %d events urls.', len(page_parameters.events_urls))

        self._events_urls.extend(page_parameters.events_urls)
    


    def _page_data(self, page_number=1) -> dict:
        """
        Return the dict of the page by page_number.
        """
        return self._page_data_cls(
            page_number=page_number, 
            event_type=self._event_type, 
            start_date=self._start_date, 
            end_date=self._end_date
        ).fetch_page_data()
