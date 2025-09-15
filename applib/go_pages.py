from applib.page_json import PageJson
from applib.response_extracting import ResponseExtracting




class GoPages:
    def __init__(self, type='live_and_upcoming', start_date='2025-09-01', end_date='2025-09-30') -> None:
        self._type = type
        self._start_date = start_date
        self._end_date = end_date



    def perform(self) -> tuple:
        total_events_urls = []

        page_dct = PageJson().retrieve(page_number=1, 
                                       type=self._type, 
                                       start_date=self._start_date, 
                                       end_date=self._end_date)

        rp = ResponseExtracting(data=page_dct)

        rp.perform()

        print('Page 1 data: ')
        print('current_page: ', rp._current_page)
        print('pages_numbers_list', rp._pages_list)
        print('events_urls', rp._events_urls)

        if rp._events_urls:
            total_events_urls.extend(rp._events_urls)
        
        print('-----' * 3)

        if not rp._pages_list:
            return tuple(total_events_urls)

        for page_number in rp._pages_list[1:]:
            page_dct = PageJson().retrieve(
                page_number=page_number, 
                type=self._type, 
                start_date=self._start_date,
                end_date=self._end_date,
                )

            rp = ResponseExtracting(data=page_dct)

            rp.perform()
            
            print(f'Page {page_number} data: ')
            print('current_page: ', rp._current_page)
            print('pages_numbers_list', rp._pages_list)
            print('events_urls', rp._events_urls)
            print('-----' * 3)

            if rp._events_urls:
                total_events_urls.extend(rp._events_urls)

        return tuple(total_events_urls)
