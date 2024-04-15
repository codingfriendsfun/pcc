# logging class for Alien Invasion

import logging
from pathlib import Path
import os

def get_log_dir(name="Logs"):
    """
    Function to locate or create a logging directory for Alien Invasion
     - Creates directory "Logs" by default.
    """

    # deal with "What folder am I working from?"
    cwd = os.getcwd()
    index = cwd.find("Alien_Invasion")
    if index > 0:
        root_dir = cwd[:index]
    else: # assume we're in root
        root_dir = cwd

    # create log dir
    log_dir = Path(f"{root_dir}/Alien_Invasion/{name}")
    if not log_dir.exists():
        os.mkdir(log_dir.resolve())

    return log_dir


class AlienLogger:
    """Logging class for Alien Invasion"""

    def __init__(self, module_name, level="INHERIT"):
        """initializing logger"""

        self.logger = logging.getLogger(module_name)
        self.log_dir = get_log_dir()

        self.levels = {
                        "INHERIT": logging.NOTSET,
                        "DEBUG": logging.DEBUG,
                        "INFO": logging.INFO,
                        "WARNING": logging.WARNING,
                        "ERROR": logging.ERROR,
                        "CRITICAL": logging.CRITICAL
        } # log levels

        self.define_log_level(level)

        if module_name == '__main__':
            logging.basicConfig(
                style='{',
                format="{asctime} {levelname} - {filename}:{lineno}: {message}",
                datefmt="%Y-%m-%d %H:%M:%S", 
                filename=f"{self.log_dir}/AlienInvasion.log", 
                filemode='w',
                level=self.log_level)
            self.logger.info("Initializing main logger.")
        else: # some other module
            self.logger.info(f"Initializing logger for {module_name}")


    def define_log_level(self, level):
        """Set log level value, regardless of logger initialization status."""

        self.log_level = self.levels[level]


    def change_log_level(self, level):
        """Update the logging level"""
        
        self.log_level = self.levels[level]
        self.logger.setLevel(self.log_level)

