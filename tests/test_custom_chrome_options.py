import unittest
from applib.custom_chrome_options import CustomChromeOptions
from selenium.webdriver.chrome.options import Options



class TestCustomChromeOptions(unittest.TestCase):
    def test_default_setup(self):
        options = CustomChromeOptions().setup()
        
        self.assertIsInstance(options, Options)
        
        self.assertEqual(1, len(options.arguments))
        self.assertIn("--disable-blink-features=AutomationControlled", options.arguments)
        
        self.assertEqual(2, len(options.experimental_options))
        self.assertIn(("excludeSwitches", ["enable-automation"]), options.experimental_options.items())
        self.assertIn(('useAutomationExtension', False), options.experimental_options.items())


    def test_when_set_user_agent(self):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
        
        options = CustomChromeOptions(user_agent=user_agent).setup()
        
        self.assertEqual(2, len(options.arguments))
        self.assertIn(f'user-agent={user_agent}', options.arguments)


    def test_add_new_options(self):
        option1 = "--headless=new"
        option2 =  "--disable-gpu"

        custom_options = CustomChromeOptions()
        custom_options.setup()
        self.assertEqual(1, len(custom_options.options.arguments))

        custom_options.add_options(option1, option2)        
        self.assertEqual(3, len(custom_options.options.arguments))
        self.assertIn(option1, custom_options.options.arguments)
        self.assertIn(option2, custom_options.options.arguments)
