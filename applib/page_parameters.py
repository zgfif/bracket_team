class PageParameters:
    def __init__(self, data: dict) -> None:
        self._content = data['content']



    @property
    def current_page(self) -> int:
        """
        Extract and return current page. it can 1, 2, ...
        """
        self._current_page = self._content['current_page']

        return self._current_page



    @property
    def pages_list(self) -> list[int]:
        """
        Extract and return pages list. It can be [1, 2, ...]
        """
        self._pages_list = self._content['pages']
        
        return self._pages_list



    @property
    def events_urls(self) -> list[str]:
        """
        Extract and return events urls. It can be [url1, url2, ..., urlN]
        """
        result = self._content['result']

        self._events_urls = [event['public_url']['absolute'] for event in result]

        return self._events_urls
