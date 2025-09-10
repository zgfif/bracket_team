from applib.extracting.base_tournament_section import BaseTournamentSection




class Location(BaseTournamentSection):    
    def extract(self) -> str:
        """
        Return the location of event from tournament info section.
        """
        location_section_element = self._nth_section_element(nth=3)
        
        if not location_section_element:
            print('Could not found location')
            return ''
        return location_section_element.text
