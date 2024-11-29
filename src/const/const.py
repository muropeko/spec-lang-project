"""
This module contains various constant values used across the application,
including prompts, error messages, and data type mappings.
"""

BASE_URL = "https://jsonplaceholder.typicode.com"

DATA_TYPES = {
    '1': 'posts',
    '2': 'users',
    '3': 'comments',
    '0': 'exit',
}

# DEFAULT
USER_CHOICE_PROMPT = "# enter: "
USER_PROMPT_WITH_VALUES = "# enter"
SAVE_CHOICE_PROMPT = "# would you like to save? (y/n): "
# ERROR_SAVING_MESSAGE = "! an error occurred while saving:"
INVALID_VALUE_MESSAGE = "! invalid value"
INVALID_CHOICE_MESSAGE = "! incorrect choice. options: "
OUT_RANGE_MESSAGE = "! value is out of a range"
# SAVE_COMPLETE_MESSAGE = "~ saved in "

# LAB 1/2
OPERATION_CHOICE_PROMPT = "# enter an operator:"
DIVISION_BY_ZERO_MESSAGE = "! division by zero cannot be done"
NEGATIVE_NUMBER_MESSAGE = "! number cannot be negative"

# LAB 3/4/5
USER_ASCII_TEXT_PROMPT = "# enter the text to generate ASCII art: "
FONT_CHOICE_PROMPT = "# choose a font: "
SIZE_CHOICE_PROMPT = "# choose a size: "
COLOR_CHOICE_PROMPT = "# choose a color: "
JUSTIFY_CHOICE_PROMPT = "# choose a justification: "
WIDTH_CHOICE_PROMPT = "# choose width of the text (10 to 175): "
FILE_NAME_PROMPT = "# enter the filename to save the art (without extension): "
CONTINUE_CHOICE_PROMPT = "# would you like to continue? (y/n): "
REPLACE_CHARACTER_PROMPT = "# enter a character to replace the symbols (or leave empty to skip): "
ONE_CHARACTER_MESSAGE = "# please enter only one character"
CALCULATE_COMPLETE_MESSAGE = "~ result: "

# LAB 7
DATA_CHOICE_MESSAGE = "# avaliable data:"
FORMAT_CHOICE_PROMPT = "# choose format (list/table): "
FILE_FORMAT_PROMPT = "# choose format for saving data (json/csv/txt): "
