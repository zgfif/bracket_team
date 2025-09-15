from applib.page_data import PageData
from applib.page_parameters import PageParameters




class EventsUrls:
    def __init__(self, type='live_and_upcoming', start_date='2025-09-01', end_date='2025-09-30') -> None:
        self._type = type
        self._start_date = start_date
        self._end_date = end_date
        self._events_urls = []
        self._pages_list = []



    def extract(self) -> tuple:
        """
        Return tuple of all events urls by specific criterias (type, start_date, end_date).
        """
        # process the first page to extract pages_list and add events_urls
        self._process_page(page_number=1)

        # if we have only one page in pages_list return
        if (len(self._pages_list) < 2):
            return tuple(self._events_urls)

        # skip the first page and process all other pages.
        for page_number in self._pages_list[1:]:
            self._process_page(page_number=page_number)

        return tuple(self._events_urls)
    


    def _process_page(self, page_number: int = 1) -> None:
        """
        Process page by page_number: extract pages_list if the page is first and collect events_urls.
        """
        page_data = self._page_data(page_number=page_number)

        page_parameters = PageParameters(data=page_data)

        if page_number == 1:
            self._pages_list = page_parameters.pages_list

        self._events_urls.extend(page_parameters.events_urls)
    


    def _page_data(self, page_number=1) -> dict:
        """
        Return the dict of the page by page_number.
        """
        return PageData().extract(
            page_number=page_number, 
            type=self._type, 
            start_date=self._start_date, 
            end_date=self._end_date)
