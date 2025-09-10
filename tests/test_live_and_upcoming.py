import unittest
from applib.live_and_upcoming import LiveAndUpcoming
from applib.events import Events


class TestLiveAndUpcoming(unittest.TestCase):
    def test_process_10_cards(self):
        events = Events()
        data = LiveAndUpcoming(driver=events.driver).process()
        self.assertEqual(len(data), 10)