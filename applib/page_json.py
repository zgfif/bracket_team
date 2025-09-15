import requests



class PageJson:
    def __init__(self) -> None:
        pass


    def retrieve(self, 
                type: str = 'live_and_upcoming',
                page_number: int = 1, 
                start_date: str ='2025-09-01', 
                end_date: str = '2025-09-30') -> dict:
        """
        Return dict with page data.
        """
        url = self._url(page_number=page_number, 
                        type=type,
                        start_date=start_date, 
                        end_date=end_date)
        
        response = requests.get(url=url, headers=self._headers())

        return response.json()



    def _headers(self) -> dict:
        return {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'X-Authorization': 'fB0SC4jghlUrszbzgFmHyAPeWvzwc5kWV3yhdP9xhs8ysLRkDDGpomh5gmqoZdAc',
        }



    def _url(self, 
             page_number: int = 1,
             type: str = 'live_and_upcoming',
             start_date: str ='2025-09-01', 
             end_date: str = '2025-09-30') -> str:
        """
        Return url for request.
        """
        return (
            'https://bracketteam.com/api/advanced-events-search?'
            f'page={page_number}&'
            'items_per_page=10&'
            f'type={type}&'
            'event_name=&venue_place_id=&'
            'sport_id=&'
            'admin_name=&'
            'team_name=&'
            'show_all_tournaments=true&'
            f'start_date={start_date}&'
            f'end_date={end_date}&'
            'user_id='
        )
