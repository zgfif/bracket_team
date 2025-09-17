import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode



load_dotenv()



class EventsApi:
    def __init__(self, 
                 page_number: int = 1, 
                 event_type: str = 'live_and_upcoming', 
                 start_date: str ='2025-09-01', 
                 end_date: str = '2025-09-30') -> None:
        self._page_number = page_number
        self._event_type = event_type
        self._start_date = start_date
        self._end_date = end_date


    def fetch_page_data(self) -> dict:
        """
        Return dict with page data.
        """
        url = self._url()

        try:
            response = requests.get(url=url, headers=self._headers(), timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(f'Request failed: {e}') from e

        try:
            return response.json()
        except ValueError:
            raise RuntimeError('Invalid JSON response')



    def _headers(self) -> dict:
        return {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'User-Agent': os.getenv('USER_AGENT', ''),
            'X-Authorization': os.getenv('AUTH_KEY', ''),
        }



    def _url(self) -> str:
        """
        Return url for request.
        """
        base = "https://bracketteam.com/api/advanced-events-search?"
        
        params = {
            'page': self._page_number,
            'items_per_page': '10',
            'type': self._event_type,
            'event_name': '',
            'venue_place_id': '',
            'sport_id': '',
            'admin_name': '',
            'team_name': '',
            'show_all_tournaments': 'true',
            'start_date': self._start_date,
            'end_date': self._end_date,
            'user_id': '',
        }

        return base + urlencode(params)