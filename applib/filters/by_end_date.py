from applib.filters.base_date import BaseDate



class ByEndDate(BaseDate):
    def _date_type(self) -> str:
        """
        Return endDate.
        """
        return 'endDate'
