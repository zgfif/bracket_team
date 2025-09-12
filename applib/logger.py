import logging
from pathlib import Path
import sys




class Logger:
    def __init__(self, logpath: str = 'logs/app.log') -> None:
        self._logpath = logpath
        
        self._prepare_logpath()
    


    def setup(self) -> logging.Logger:
        """
        Return logger which saves logs to file and prints in console.
        """
        logger = logging.getLogger(__name__)

        logger.setLevel(level=logging.INFO)

        for handler in [self._file_handler(), self._console_handler()]:
            logger.addHandler(handler)

        return logger



    def _prepare_logpath(self) -> None:
        """
        Prepare folder for log file.
        """
        Path(self._logpath).parent.mkdir(parents=True, exist_ok=True)



    def _formatter(self) -> logging.Formatter:
        """
        Return formatter for logs.
        """
        return logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s",
            style="%",
        )



    def _file_handler(self) -> logging.FileHandler:
        """
        Return configured file handler.
        """
        file_handler = logging.FileHandler(self._logpath, mode='a', encoding='UTF-8')

        file_handler.setFormatter(self._formatter())

        file_handler.setLevel(level=logging.INFO)
        
        return file_handler
    


    def _console_handler(self) -> logging.StreamHandler:
        """
        Return configured console handler.
        """
        console_handler = logging.StreamHandler(stream=sys.stdout)

        console_handler.setFormatter(self._formatter())

        console_handler.setLevel(level=logging.INFO)

        return console_handler
