import unittest
from applib.events import Events
from applib.completed_tab import CompletedTab




class TestCompletedTab(unittest.TestCase):
    def test_switch_tab(self):
        events = Events()
        CompletedTab(driver=events.driver, logger=events.logger).switch()
