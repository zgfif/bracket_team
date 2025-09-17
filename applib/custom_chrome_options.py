from selenium.webdriver.chrome.options import Options




class CustomChromeOptions:
    def __init__(self, user_agent: str | None = None) -> None:
        self.options = Options()
        self.user_agent = user_agent


    def setup(self) -> Options:
        """
        Setup options for Google Chrome.
        """
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        if self.user_agent:
            self.options.add_argument(f"user-agent={self.user_agent}")

        return self.options


    def add_options(self, *args: str) -> None:
        """
        Add custom Chrome arguments.
        Example: add_arguments("--headless=new", "--disable-gpu")
        """
        for arg in args:
            self.options.add_argument(arg)
