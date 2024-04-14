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
    # else do nothing, assume we're in root

    # create log dir
    log_dir = Path(f"{root_dir}/Alien_Invasion/{name}")
    if not log_dir.exists():
        os.mkdir(log_dir.resolve())

    return log_dir
    

class AlienLogger:
    """Logging class for Alien Invasion"""

    def __init__(self, module_name, level=logging.NOTSET):
        """initializing logger"""
        self.logger = logging.getLogger(module_name)
        self.log_dir = get_log_dir()

        if module_name == '__main__':
            logging.basicConfig(filename=self.log_dir, level=level)
            self.logger.info("Initializing main logger.")

