import unittest
from applib.events import Events
from applib.pass_pages import PassPages
from applib.filter import Filter
from applib.completed_tab import CompletedTab



class TestPassPages(unittest.TestCase):
    def test_pass_pages(self):
        events = Events()

        Filter(driver=events.driver, logger=events.logger).apply(
            published=True,
            sport=None,
            start_date='9/1/2025',
            end_date='9/30/2025',
        )
        
        PassPages(driver=events.driver, 
                  tabname='Live and Upcoming', 
                  logger=events.logger, 
                  filepath='09012025_30012025.xlsx').perform()
        
        CompletedTab(driver=events.driver, logger=events.logger).switch()

        
        PassPages(driver=events.driver, 
                  tabname='Completed', 
                  logger=events.logger, 
                  filepath='09012025_30012025.xlsx').perform()
