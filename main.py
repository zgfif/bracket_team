from applib.events import Events
from applib.filter import Filter
from applib.pass_pages import PassPages
from applib.completed_tab import CompletedTab




def main():
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
              filepath='total_0901025_09302025.xlsx').perform()
    
    CompletedTab(driver=events.driver, 
                 logger=events.logger).switch()

    PassPages(driver=events.driver, 
              tabname='Completed', 
              logger=events.logger,
              filepath='total_0901025_09302025.xlsx').perform()



if __name__ == '__main__':
    main()
