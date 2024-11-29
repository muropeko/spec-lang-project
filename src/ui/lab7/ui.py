"""
User Interface module for displaying and managing user interactions.

Provides functions to display options, get user input, and format data display.
"""

from tabulate import tabulate
from src.const.const import (
    DATA_TYPES, USER_CHOICE_PROMPT, INVALID_CHOICE_MESSAGE, FORMAT_CHOICE_PROMPT,
    DATA_CHOICE_MESSAGE, SAVE_CHOICE_PROMPT, FILE_FORMAT_PROMPT, FILE_NAME_PROMPT
)
from lib.user_input import UserInput


class UserInterface:
    """Class to handle user interactions and data display options."""

    # (rest of your methods)

    @staticmethod
    def display_options():
        """Displays the available data type options to the user."""
        print(f"\n{DATA_CHOICE_MESSAGE}")
        for data_type in DATA_TYPES.keys():
            print(f"\t {data_type}. {DATA_TYPES[data_type]}")

    @staticmethod
    def get_user_choice():
        """
        Prompts the user to choose a data type.
        Returns:
            str: Selected data type or None if exiting.
        """
        UserInterface.display_options()
        choice = UserInput.get_input(USER_CHOICE_PROMPT, DATA_TYPES.keys())
        if choice == '0':
            print("BYEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            return None
        if choice in DATA_TYPES:
            return DATA_TYPES[choice]
        return None

    @staticmethod
    def display_list(data):
        """
        Displays data in a list format.
        Args:
            data (list): List of data items to display.
        """
        if not data:
            print("...empty :(")
            return
        for index, item in enumerate(data, start=1):
            print(f"{index}. {item}")

    @staticmethod
    def display_table(data):
        """
        Displays data in a table format using 'tabulate'.
        Args:
            data (list of dicts): List of data dictionaries to display.
        """
        headers = data[0].keys() if data else []
        table_data = [list(item.values()) for item in data]
        print(tabulate(table_data, headers, tablefmt="grid"))

    @staticmethod
    def get_display_format():
        """
        Prompts the user to choose a display format.
        Returns:
            str: The chosen display format (e.g., 'list' or 'table').
        """
        format_choice = UserInput.get_input(FORMAT_CHOICE_PROMPT)
        return format_choice.lower()

    @staticmethod
    def display_data(data):
        """
        Displays data based on the user-chosen format.
        Args:
            data (list): Data to display, either in list or table format.
        """
        format_choice = UserInterface.get_display_format()
        display_methods = {
            "list": UserInterface.display_list,
            "table": UserInterface.display_table,
        }
        display_method = display_methods.get(format_choice)

        if display_method:
            display_method(data)
        else:
            print(INVALID_CHOICE_MESSAGE)

    @staticmethod
    def ask_save_data():
        """
        Asks the user whether to save the data.
        Returns:
            bool: True if the user agrees to save, False otherwise.
        """
        response = UserInput.get_input(SAVE_CHOICE_PROMPT).lower()
        return response in ['yes', 'y']

    @staticmethod
    def get_save_options():
        """
        Prompts the user for save format and filename.
        Returns:
            tuple: Format choice (e.g., 'json') and filename.
        """
        format_choice = UserInput.get_input(FILE_FORMAT_PROMPT, ["json", "csv", "txt"])
        filename = UserInput.get_input(FILE_NAME_PROMPT)
        return format_choice, filename
