from applib.extracting.base_tournament_section import BaseTournamentSection



class Sport(BaseTournamentSection):
    def extract(self) -> str:
        """
        Return the kind of sport of event from tournament info section.
        """
        sport_section_element = self._nth_section_element(nth=1)
        
        if not sport_section_element:
            print('Could not found sport section element.')
            return ''
        
        return  sport_section_element.text    
