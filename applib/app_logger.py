import logging
from pathlib import Path
import sys




class AppLogger:
    def __init__(self, logpath: str = 'logs/app.log', level: int = logging.INFO) -> None:
        self._logpath = logpath
        self._level = level
        self._prepare_logpath()

        self._formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(message)s", 
            style="%",
        )
        
    


    def setup(self, name: str = '') -> logging.Logger:
        """
        Return logger which saves logs to file and prints in console.
        """
        logger = logging.getLogger(name or __name__)
        logger.setLevel(level=self._level)
        
        if not logger.handlers:
            for handler in self._file_handler(), self._console_handler():
                logger.addHandler(handler)

        return logger



    def _prepare_logpath(self) -> None:
        """
        Prepare folder for log file.
        """
        Path(self._logpath).parent.mkdir(parents=True, exist_ok=True)



    def _file_handler(self) -> logging.FileHandler:
        """
        Return configured file handler.
        """
        file_handler = logging.FileHandler(self._logpath, mode='a', encoding='UTF-8')

        file_handler.setFormatter(self._formatter)

        file_handler.setLevel(level=self._level)
        
        return file_handler
    


    def _console_handler(self) -> logging.StreamHandler:
        """
        Return configured console handler.
        """
        console_handler = logging.StreamHandler(stream=sys.stdout)

        console_handler.setFormatter(self._formatter)

        console_handler.setLevel(level=self._level)

        return console_handler
