"""
This module contains the configuration settings for Lab 3, including font styles, 
colors, and file paths used for saving the results.
"""

from src.classes.lab3.config import BaseConfig
from src.const.path_constants import FOLDER_PATH_RESULT_LAB3

class Lab3Config(BaseConfig):
    """
    Configuration class for Lab 3 that extends BaseConfig.
    Adds specific fonts, colors, and file paths for Lab 3 operations.
    """

    def __init__(self):
        super().__init__()
        self.fonts.extend(['epic', 'starwars'])
        self.colors.update({
            'red': "\033[31m",
            'green': "\033[32m",
            'blue': "\033[34m",
            'reset': "\033[0m"
        })
        self.fixed_width = 175
        self.file_path = FOLDER_PATH_RESULT_LAB3

    def configure(self):
        """
        Placeholder method to avoid the "too-few-public-methods" warning.
        This method can be extended later if additional configuration is needed.
        """
        pass
