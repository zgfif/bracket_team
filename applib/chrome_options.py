from selenium.webdriver.chrome.options import Options




class ChromeOptions:
    def __init__(self) -> None:
        self.options = Options()



    def setup(self) -> Options:
        """
        Setup options for Google Chrome.
        """
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
            )

        return self.options
