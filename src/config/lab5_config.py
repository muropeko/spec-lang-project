from src.classes.lab3.config import BaseConfig
from src.const.path_constants import FOLDER_PATH_RESULT_LAB5

class Lab5Config(BaseConfig):
    def __init__(self):
        super().__init__()
        self.colors.update({
            "red": "\033[31m",
            "orange": "\033[33m",
            "yellow": "\033[32m",
            "cyan": "\033[36m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            'reset': "\033[0m"
        })
        self.fixed_width = 175
        self.file_path = FOLDER_PATH_RESULT_LAB5
