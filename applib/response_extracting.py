class ResponseExtracting:
    def __init__(self, data: dict) -> None:
        self._data = data
        self._current_page = None
        self._pages_list = None
        self.events_urls = None



    def perform(self) -> None:
        """
        Find _current_page, _pages_list and _events_urls.
        """
        self._current_page = self._data['content']['current_page']
        
        self._pages_list = self._data['content']['pages']
        
        self._extract_events_urls()



    def _extract_events_urls(self) -> None:
        result = self._data['content']['result']

        self._events_urls = [event['public_url']['absolute'] for event in result]
