from src.classes.lab3.config import BaseConfig
from src.classes.lab4.custom_font import font
from src.classes.lab4.star_font import star_font
from src.const.path_constants import FOLDER_PATH_RESULT_LAB4


class Lab4Config(BaseConfig):
    def __init__(self):
        super().__init__()
        self.fonts.extend(["star", "custom"])
        self.custom_font = font
        self.star_font = star_font
        self.colors.update({
            'black': "\033[30m",
            'white': "\033[37m",
            'light_gray': "\033[37m",
            'dark_gray': "\033[90m",
            'reset': "\033[0m"
        })
        self.fixed_width = 175
        self.file_path = FOLDER_PATH_RESULT_LAB4